use std::{cmp::max, cmp::min, fs};

pub fn merge_intervals(intervals: Vec<(u64, u64)>) -> Vec<(u64, u64)> {
    let mut res: Vec<(u64, u64)> = vec![];

    for i in 0..intervals.len() {
        if res.len() == 0 {
            res.push(intervals[i]);
            continue;
        }

        if res[res.len() - 1].1 >= intervals[i].0 {
            let last = res.pop().unwrap();
            res.push((min(last.0, intervals[i].0), max(last.1, intervals[i].1)));
        } else {
            res.push(intervals[i]);
        }
    }
    res
}

pub fn day5(filename: &str) -> (i64, u64) {
    let contents = fs::read_to_string(filename).expect("could not open input file");

    let mut lines = contents.lines();
    let mut intervals: Vec<(u64, u64)> = vec![];

    while let Some(line) = lines.next() {
        if line == "" {
            break;
        }

        let entry: Vec<u64> = line.trim().split("-").map(|x| x.parse().unwrap()).collect();
        intervals.push((entry[0], entry[1]));
    }
    intervals.sort_by_key(|x| x.0);
    let res = merge_intervals(intervals);
    let mut fresh = 0;
    let mut fresh_count = 0;

    while let Some(line) = lines.next() {
        let number: u64 = line.trim().parse().unwrap();

        for i in 0..res.len() {
            if number < res[i].0 {
                break;
            }

            if number > res[i].1 {
                continue;
            }

            fresh += 1;
            break;
        }
    }

    for i in 0..res.len() {
        fresh_count += (res[i].1 - res[i].0) + 1
    }
    (fresh, fresh_count)
}
