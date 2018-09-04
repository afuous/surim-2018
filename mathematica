(*

This expression calculates the variance of A_{n,k}.

Mathematica is available on the stanford servers; it can be run like so:

ssh <username>@rice.stanford.edu
module load mathematica
math

output:

                        3      2                          2                    2
-((-2 + k) (-1 + k) k (k  - 3 k  (-1 + n) - n (2 - 3 n + n ) + k (2 - 6 n + 3 n )))
-----------------------------------------------------------------------------------
                                                       2
                           2 (-4 + n) (-3 + n) (-2 + n)

*)

Simplify[(k(k-1)(k-2)(k-3)(k-4)(k-5)/(n(n-1)(n-2)(n-3)(n-4)(n-5))) (1/4)(n^4 - 11n^3 + 35n^2 - 25n) + (k(k-1)(k-2)(k-3)(k-4)/(n(n-1)(n-2)(n-3)(n-4))) (1/4)(9n^3 - 48n^2 + 39n) + (k(k-1)(k-2)(k-3)/(n(n-1)(n-2)(n-3))) (3)(n^2 - n) + (k(k-1)(k-2)/(n(n-1)(n-2))) (1/2)(n^2 - n) - ((k(k-1)(k-2)/(n(n-1)(n-2))) (1/2)(n^2-n))^2]
