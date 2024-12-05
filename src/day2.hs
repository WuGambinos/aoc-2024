import Control.Arrow (Arrow (second))
import Data.IntMap (delete)
import System.IO

-- allPositive :: [Int] -> Bool
-- allPositive = foldr (\x acc -> x > 0 && acc) True

deleteN :: Int -> [a] -> [a]
deleteN _ [] = []
deleteN i (a : as)
  | i == 0 = as
  | otherwise = a : deleteN (i - 1) as

convertLineToIntList :: String -> [Int]
convertLineToIntList line = map read (words line)

checkCondition1 :: [Int] -> Bool
checkCondition1 lst = all (\(x, y) -> x > y && (x - y >= 1 && x - y <= 3)) (zip lst (tail lst))

checkCondition2 :: [Int] -> Bool
checkCondition2 lst = all (\(x, y) -> x < y && (y - x >= 1 && y - x <= 3)) (zip lst (tail lst))

-- Part 1
valid :: [[Int]] -> Int
valid =
  foldr
    ( \lst acc ->
        if checkCondition1 lst || checkCondition2 lst
          then
            acc + 1
          else
            acc
    )
    0

-- Part 2
secondCheck :: [Int] -> Int -> Bool -> Bool
secondCheck lst idx acc =
  if idx == length lst
    then
      acc
    else
      let copy_lst = deleteN idx lst
       in let new_bool = checkCondition1 copy_lst || checkCondition2 copy_lst
           in secondCheck lst (idx + 1) (acc || new_bool)

valid2 :: [[Int]] -> Int
valid2 =
  foldr
    ( \row acc ->
        (if (checkCondition1 row || checkCondition2 row) || secondCheck row 0 False then acc + 1 else acc)
    )
    0

main :: IO ()
main = do
  content <- readFile "day2.txt"

  let linesList = map convertLineToIntList (lines content)
  let day1 = valid linesList
  let day2 = valid2 linesList
  let element = linesList !! 2
  let check = checkCondition1 element || checkCondition2 element
  let lst = [1, 2]

  putStr "DAY 1: "
  print $ valid linesList

  putStr "DAY 2: "
  print $ valid2 linesList