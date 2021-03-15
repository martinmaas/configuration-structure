import re
import sys

content = ''.join(sys.stdin.readlines())

type_replace = {}

def replace_enums(m):
  if not re.search(r'option[\n\r\s]+\(bitmap\)', m.group(0)):
    return m.group(0)

  enum_body = 'None = 0; '
  current_id = 1
  for e in m.group(2).split(';'):
    m2 = re.match(r'[\n\r\s]+(\S+)[\n\r\s]+=', e)
    if m2:
      enum_body += '%s = %d; ' % (m2.group(1), current_id)
      current_id *= 2

  type_replace[m.group(1)] = 'uint32' if (current_id < 2 ** 32) else 'uint64'
  return 'enum %s { %s}' % (m.group(1), enum_body)

# TODO: Handle comments within the enum.
transformed = re.sub(r'enum[\n\r\s]*(\S+)[\n\r\s]+\{(.*?)\}', replace_enums, content, flags=re.S)

# TODO: This is very brittle, needs to be handled using proper parsing code.
for k,v in type_replace.items():
  transformed = re.sub('^(\s+)' + k, v, transformed, flags=re.MULTILINE)

print(transformed)
