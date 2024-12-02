let read_file (file : string) =
  In_channel.with_open_bin file In_channel.input_all

let list_from_file_str (file : string) =
  List.filter
    (fun x -> x |> String.length > 0)
    (String.split_on_char '\n' (read_file file))

let lines = list_from_file_str "day2_test.txt"

(*
let _ = List.iter (fun x -> print_endline x) lines
*)

let convert_to_list_of_lists input =
  List.map
    (fun str ->
      str
      |> String.split_on_char ' ' (* Split the string by spaces *)
      |> List.filter (fun s -> s <> "") (* Remove empty strings, if any *)
      |> List.map int_of_string (* Convert each substring to an integer *))
    input

let print_list_of_lists list_of_lists =
  let print_list lst =
    lst
    |> List.map string_of_int (* Convert each number to a string *)
    |> String.concat "; " (* Join the numbers with "; " *)
    |> Printf.printf "[%s]" (* Print the formatted list *)
  in
  Printf.printf "[";
  list_of_lists
  |> List.iteri (fun i lst ->
         if i > 0 then Printf.printf "; ";
         (* Add separator for lists *)
         print_list lst);
  Printf.printf "]\n"

let fold_2d_list f acc list_of_lists =
  List.fold_left
    (fun acc inner_list -> List.fold_left f acc inner_list)
    acc list_of_lists

(* Helper to check if a list is strictly increasing *)
let is_strictly_increasing lst =
  match lst with
  | [] | [ _ ] ->
      false (* Empty or single-element lists cannot be strictly increasing *)
  | _ -> List.for_all2 ( < ) lst (List.tl lst)

(* Helper to check if a list is strictly decreasing *)
let is_strictly_decreasing lst =
  match lst with
  | [] | [ _ ] ->
      false (* Empty or single-element lists cannot be strictly decreasing *)
  | _ -> List.for_all2 ( > ) lst (List.tl lst)

(* Check each row for increasing or decreasing *)
let check_rows list_of_lists =
  List.map
    (fun row ->
      if is_strictly_increasing row then `Increasing
      else if is_strictly_decreasing row then `Decreasing
      else `Neither)
    list_of_lists

(* DAY1 *)
let _ =
  let lst_of_lst = convert_to_list_of_lists lines in
  let sum = fold_2d_list (fun acc x -> acc + x) 0 lst_of_lst in
  let _ = Printf.printf "%d\n" sum in
  let res = check_rows lst_of_lst in
  let _ =
    List.iter
      (fun x ->
        match x with
        | `Increasing -> Printf.printf "Increasing\n"
        | `Decreasing -> Printf.printf "Decreasing\n"
        | `Neither -> Printf.printf "Neither\n")
      res
  in
  ()
(*
    let num_list = List.map int_of_string num_lst in
    List.iter (fun x -> Printf.printf "%d " x) num_list
    *)
