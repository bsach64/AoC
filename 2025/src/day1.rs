use std::fs;

pub fn part1(filename: &str) -> u64 {
    let contents = fs::read_to_string(filename)
        .expect("could not open input file");

    let lines = contents.lines();
    let mut res = 0;
    let mut cur = 50;

    for line in lines {
        let mut chars = line.chars();

        match chars.nth(0).expect("did not get direction") {
            'L' => {
                let diff: i64 = chars.as_str().parse().expect("could not get integer");
                for _ in 0..diff {
                    assert!(cur >= 0 && cur <= 99, "value of cur: {}", cur);
                    if cur == 0 {
                        cur = 99;
                    } else {
                        cur -= 1;
                        if cur == 0 {
                            res += 1;
                        }
                    }
                }
            },
            'R' => {
                let diff: i64 = chars.as_str().parse().expect("could not get integer");
                for _ in 0..diff {
                    assert!(cur >= 0 && cur <= 99);
                    cur += 1;
                    if cur == 100 {
                        res += 1;
                        cur = 0;
                    }
                }
            },
            _ => println!("Invalid Direction")
        }
    }
    res
}

pub fn part2(_filename: &str) -> u64 {
    0
}