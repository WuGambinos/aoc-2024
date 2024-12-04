let read_file (file : string) =
  In_channel.with_open_bin file In_channel.input_all

let list_from_file_str (file : string) =
  List.filter
    (fun x -> x |> String.length > 0)
    (String.split_on_char '\n' (read_file file))

let lines = list_from_file_str "day2.txt"
let _ = List.iter (fun x -> print_endline x) lines

let convert_to_list_of_lists input =
  List.map
    (fun str ->
      str
      |> String.split_on_char ' ' (* Split the string by spaces *)
      |> List.filter (fun s -> s <> "") (* Remove empty strings, if any *)
      |> List.map int_of_string (* Convert each substring to an integer *))
    input

let rec increasing lst =
  match lst with
  | [] -> true
  | [ _ ] -> true
  | x :: y :: rest ->
      x < y && (y - x >= 1 && y - x <= 3) && increasing (y :: rest)

let rec decreasing lst =
  match lst with
  | [] -> true
  | [ _ ] -> true
  | x :: y :: rest ->
      x > y && (x - y >= 1 && x - y <= 3) && decreasing (y :: rest)

(* Day 1 *)
let day1 lines =
  List.fold_right
    (fun item acc ->
      if increasing item || decreasing item then acc + 1 else acc)
    lines 0

(* Day 2 *)
let rec second_check lst idx acc =
  if idx == List.length lst then acc
  else
    let copy_lst = List.filteri (fun i item -> i != idx) lst in
    let new_bool = increasing copy_lst || decreasing copy_lst in
    second_check lst (idx + 1) (acc || new_bool)

let day2 lines =
  List.fold_right
    (fun row acc ->
      if (increasing row || decreasing row) || second_check row 0 false then
        acc + 1
      else acc)
    lines 0

let _ =
  let lines = convert_to_list_of_lists lines in
  let day1_answer = day1 lines in
  let day2_answer = day2 lines in
  let _ = Printf.printf "DAY 1: %d\n" day1_answer in
  let _ = Printf.printf "DAY 2: %d\n" day2_answer in
  ()
