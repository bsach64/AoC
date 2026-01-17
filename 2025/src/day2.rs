use std::fs;

fn is_invalid(num: i64) -> bool {
    let num_str = num.to_string();

    if num_str.len() % 2 != 0 {
        return false;
    }

    let mid = num_str.chars().count() / 2;

    let mid_byte = num_str
        .char_indices()
        .nth(mid)
        .map(|(i, _)| i)
        .unwrap_or(num_str.len());

    let (first, second) = num_str.split_at(mid_byte);
    first == second
}

fn is_crazy_invalid(num: i64) -> bool {
    let num_str = num.to_string();
    let chars: Vec<char> = num_str.chars().collect();
    let n = chars.len();

    for chunk_len in 1..n {
        if n % chunk_len != 0 {
            continue;
        }
        let chunks: Vec<String> = chars
            .chunks(chunk_len)
            .map(|c| c.iter().collect())
            .collect();

        let mut failed = false;

        let first = chunks[0].clone();
        for x in chunks {
            if x != first {
                failed = true;
                break;
            }
        }

        if !failed {
            return true;
        }
    }
    false
}

pub fn part1(filename: &str) -> i64 {
    let contents = fs::read_to_string(filename).expect("could not open input file");

    let mut part1 = Vec::<i64>::new();
    let pairs = contents
        .split(",")
        .filter_map(|c| {
            c.trim().split_once('-').and_then(|(l, r)| {
                Some((
                    l.parse::<i64>().ok().expect("Nope"),
                    r.parse::<i64>().ok().expect("Nope"),
                ))
            })
        })
        .collect::<Vec<(i64, i64)>>();

    for p in &pairs {
        for num in p.0..p.1 + 1 {
            if is_invalid(num) {
                part1.push(num);
            }
        }
    }

    part1.iter().sum()
}

pub fn part2(filename: &str) -> i64 {
    let contents = fs::read_to_string(filename).expect("could not open input file");

    let mut part2 = Vec::<i64>::new();
    let pairs = contents
        .split(",")
        .filter_map(|c| {
            c.trim().split_once('-').and_then(|(l, r)| {
                Some((
                    l.parse::<i64>().ok().expect("Nope"),
                    r.parse::<i64>().ok().expect("Nope"),
                ))
            })
        })
        .collect::<Vec<(i64, i64)>>();

    for p in &pairs {
        for num in p.0..p.1 + 1 {
            if is_crazy_invalid(num) {
                part2.push(num);
            }
        }
    }

    part2.iter().sum()
}
