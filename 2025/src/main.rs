mod day1;
mod day2;
mod day3;

fn main() {
    println!("Day 1 Part 1: {}", day1::part1("src/1.txt"));
    println!("Day 1 Part 2: {}", day1::part2("src/1.txt"));
    println!("Day 2 Part 1: {}", day2::part1("src/2.txt"));
    println!("Day 2 Part 2: {}", day2::part2("src/2.txt"));
    println!("Day 3 Part 1: {}", day3::part1("src/3.txt"));
    println!("Day 3 Part 2: {}", day3::part2("src/3.txt"));
}
