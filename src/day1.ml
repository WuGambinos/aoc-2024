let read_file (file : string) = In_channel.with_open_bin file In_channel.input_all
let list_from_file_str (file : string) =
      List.filter
          (fun x -> x |> String.length > 0)
              (String.split_on_char '\n' (read_file file))
;;

let lines = list_from_file_str "day1.txt"

(* DAY 1 PART 1 *)
let _ = 
    let left_lst = List.fold_left (fun acc item -> 
    let left = item |> String.split_on_char ' ' |> List.hd |> int_of_string   in
    left::acc) [] lines in

    let right_lst = List.fold_left (fun acc item -> 
    let split = String.split_on_char ' ' item in
    let right =  int_of_string (List.nth split (List.length split - 1))    in
    right::acc) [] lines in

    let left_lst = List.sort compare left_lst in
    let right_lst = List.sort compare right_lst in
    let res = List.fold_left2 (fun acc x y -> 
        acc + Int.abs(y - x)) 0 left_lst right_lst in
    Printf.printf "DAY 1: %d\n" res;


(* DAY 1 PART 2 *)
let _ = ()
