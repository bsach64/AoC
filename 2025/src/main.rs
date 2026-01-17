mod day1;
mod day2;
mod day3;
mod day4;
mod day5;
mod day6;

fn main() {
    println!("Day 1 Part 1: {}", day1::part1("src/1.txt"));
    println!("Day 1 Part 2: {}", day1::part2("src/1.txt"));
    println!("Day 2 Part 1: {}", day2::part1("src/2.txt"));
    println!("Day 2 Part 2: {}", day2::part2("src/2.txt"));
    println!("Day 3 Part 1: {}", day3::part1("src/3.txt"));
    println!("Day 3 Part 2: {}", day3::part2("src/3.txt"));
    println!("Day 4 Part 1: {}", day4::part1("src/4.txt"));
    println!("Day 4 Part 2: {}", day4::part2("src/4.txt"));
    println!("Day 5 Part 1: {:?}", day5::day5("src/5.txt"));
    println!("Day 6 Part 1: {:?}", day6::part1("src/6.txt"));
    println!("Day 6 Part 2: {:?}", day6::part2("src/6.txt"));
}
