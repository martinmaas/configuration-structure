#include "example.pb.h"

int main() {
  riscv::Privileged p;
  p.set_modes(riscv::Privileged_Mode_M | riscv::Privileged_Mode_S);
  if (p.modes() & riscv::Privileged_Mode_M) printf("M bit present\n");
  return 0;
}
