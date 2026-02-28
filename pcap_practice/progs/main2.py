import sys
# for p in sys.path:
#     print(p)

sys.path.append('../packages')
import extra.iota
from extra.good.best.tau import funT
import extra.good.best.sigma

print(extra.iota.funI())
print(extra.good.best.sigma.funS())
print(funT())