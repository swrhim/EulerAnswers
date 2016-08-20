let upperBound = 4000000

let fibSeq = Seq.unfold(fun (a,b) -> Some (a, (b, a+b))) (0, 1)
let total = 
    fibSeq 
    |> Seq.takeWhile(fun x -> x <= upperBound) 
    |> Seq.filter(fun n -> n % 2 = 0)
    |> Seq.sum

sprintf "%i" total