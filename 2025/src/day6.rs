use std::{fs, num};

pub fn part1(filename: &str) -> u64 {
    let contents = fs::read_to_string(filename).expect("could not open file");

    let mut lines = contents.lines();

    let mut numbers: Vec<Vec<u64>> = vec![];
    let mut operations: Vec<char> = vec![];
    let mut res = 0;

    while let Some(line) = lines.next() {
        let char = line.chars().peekable().nth(0).unwrap();
        if char == '*' || char == '+' {
            operations = line
                .trim()
                .split(" ")
                .filter_map(|x| match x.chars().next() {
                    Some(c) => {
                        if c.is_whitespace() {
                            None
                        } else {
                            Some(c)
                        }
                    }
                    None => None,
                })
                .collect();
        }

        let row: Vec<u64> = line
            .trim()
            .split(" ")
            .filter_map(|x| x.trim().parse().ok())
            .collect();
        if row.len() > 0 {
            numbers.push(row);
        }
    }

    assert_eq!(numbers[0].len(), operations.len());
    for i in 0..numbers[0].len() {
        if operations[i] == '*' {
            res += numbers[0][i] * numbers[1][i] * numbers[2][i] * numbers[3][i];
        } else {
            res += numbers[0][i] + numbers[1][i] + numbers[2][i] + numbers[3][i];
        }
    }
    res
}

pub fn part2(filename: &str) -> u64 {
    let contents = fs::read_to_string(filename).expect("could not open file");
    let lines: Vec<&str> = contents.lines().into_iter().collect();
    let mut res = 0;
    let mut numbers: Vec<u64> = vec![];
    let mut op: char = ' ';

    for i in (0..lines[0].len()).rev() {
        let mut letters: Vec<char> = vec![];
        for j in 0..5 {
            letters.push(lines[j].chars().nth(i).unwrap());
        }

        let num: Option<u64> = format!("{}{}{}{}", letters[0], letters[1], letters[2], letters[3]).trim().parse().ok();
        if let Some(x) = num {
            numbers.push(x);
        }
        if letters[4] != ' ' {
            op = letters[4];
        }
        let is_whitespace = letters.iter().all(|x| x.is_whitespace());
        if is_whitespace || i == 0 {
            assert!(op == '*' || op == '+');
            if op == '+' {
                let sum: u64 = numbers.iter().sum();
                res += sum;
            } else {
                let mul: u64 = numbers.iter().product();
                res += mul;
            }
            op = ' ';
            numbers = vec![];
        }
    }
    res
}
