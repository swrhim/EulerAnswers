let nums = [ 0..999]
nums |> List.fold(fun acc num -> if (num % 3 = 0 || num % 5 = 0) then acc + num else acc) 0
