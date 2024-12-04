let read_file (file : string) =
  In_channel.with_open_bin file In_channel.input_all

let list_from_file_str (file : string) =
  List.filter
    (fun x -> x |> String.length > 0)
    (String.split_on_char '\n' (read_file file))

let is_digit (ch : char) = match ch with '0' .. '9' -> true | _ -> false

let rec parse_number (s : string) (idx : int) (acc : string) =
  let digit = String.get s idx in
  if is_digit digit then
    parse_number s (idx + 1) (acc ^ Printf.sprintf "%c" digit)
  else (idx, acc)

let check (s : string) (first_num : string) (second_num : string) (state : int)
    (acc : int) (idx : int) =
  if idx + 3 > String.length s then (s, first_num, second_num, 6, acc, idx + 1)
  else if String.equal (String.sub s idx 3) "mul" then
    (s, first_num, second_num, 1, acc, idx + 3)
  else if state == 1 && Char.equal (String.get s idx) '(' then
    (s, first_num, second_num, 2, acc, idx + 1)
  else if state == 2 && is_digit (String.get s idx) then
    let new_idx, new_first_num = parse_number s idx String.empty in
    (s, new_first_num, second_num, 3, acc, new_idx)
  else if state == 3 && Char.equal (String.get s idx) ',' then
    (s, first_num, second_num, 4, acc, idx + 1)
  else if state == 4 && is_digit (String.get s idx) then
    let new_idx, new_second_num = parse_number s idx String.empty in
    (s, first_num, new_second_num, 5, acc, new_idx)
  else if state == 5 && Char.equal (String.get s idx) ')' then
    (s, first_num, second_num, 6, acc, idx + 1)
  else (s, first_num, second_num, state, acc, idx + 1)

let rec help_parse_memory (s : string) (first_num : string)
    (second_num : string) (state : int) (acc : int) (idx : int) =
  if idx == String.length s then acc
  else if state == 6 then
    (*
    let _ = Printf.printf "LENTGH: %d\n\n" (String.length s) in
    *)
    let n1 = int_of_string first_num in
    let n2 = int_of_string second_num in
    let _ = Printf.printf "mul(%d,%d)\n" n1 n2 in
    help_parse_memory s first_num second_num 0 (acc + (n1 * n2)) idx
  else
    let new_s, new_first_num, new_second_num, new_state, new_acc, new_idx =
      check s first_num second_num state acc idx
    in
    (*
    let _ =
      Printf.printf "IDX: %d NUM: %s NUM: %s\n" idx new_first_num new_second_num
    in
      *)
    help_parse_memory new_s new_first_num new_second_num new_state new_acc
      new_idx

let parse_memory input =
  let _res = help_parse_memory input "" "" 0 0 0 in
  Printf.printf " RES: %d" _res;
  ()

let input = read_file "day3.txt"
let _ = parse_memory input
