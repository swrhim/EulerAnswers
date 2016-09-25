let upperBound = 4000000

let fibSeq = Seq.unfold(fun (a,b) -> if a <= upperBound then Some (a, (b, a+b)) else None) (0, 1)
let total = 
    fibSeq 
    |> Seq.filter(fun n -> n % 2 = 0)
    |> Seq.sum

sprintf "%i" total
