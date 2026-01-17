use std::fs;

// no ai can generate code like this
fn check_surrounding(i: usize, j: usize, grid: &Vec<Vec<char>>) -> u32 {
    let mut count = 0;

    if j > 0 && grid[i][j - 1] == '@' {
        count += 1;
    }
    if j < grid[i].len() - 1 && grid[i][j + 1] == '@' {
        count += 1;
    }
    if i > 0 && grid[i - 1][j] == '@' {
        count += 1;
    }
    if i < grid.len() - 1 && grid[i+1][j] == '@' {
        count += 1;
    }
    if j > 0 && i > 0 && grid[i - 1][j - 1] == '@' {
        count += 1;
    }
    if j < grid[i].len() - 1 && i < grid.len() - 1 && grid[i+1][j+1] == '@' {
        count += 1;
    }
    if j > 0 && i < grid.len() - 1 && grid[i+1][j - 1] == '@' {
        count += 1;
    }
    if i > 0 && j < grid[i].len() - 1 && grid[i-1][j+1] == '@' {
        count += 1;
    }
    count
}

pub fn part1(filename: &str) -> i64 {
    let contents = fs::read_to_string(filename)
        .expect("could not open input file");

    let mut res = 0;
    let grid: Vec<Vec<char>> = contents.lines()
        .map(|line| line.chars().collect())
        .collect();

    for (i, line) in grid.iter().enumerate() {
        for (j, char) in line.iter().enumerate() {
            if char == &'@' && check_surrounding(i, j, &grid) < 4 {
                res += 1;
            }
        }
    }
    res
}

pub fn part2(filename: &str) -> i64 {
    let contents = fs::read_to_string(filename)
        .expect("could not open input file");

    let mut cur = 0;
    let mut res = 0;
    let mut grid: Vec<Vec<char>> = contents.lines()
        .map(|line| line.chars().collect())
        .collect();

    loop {
        let mut updates: Vec<(usize, usize)> = vec![];
        for (i, line) in grid.iter().enumerate() {
            for (j, char) in line.iter().enumerate() {
                if char == &'@' && check_surrounding(i, j, &grid) < 4 {
                    cur += 1;
                    updates.push((i, j));
                }
            }
        }

        for entry in updates {
            grid[entry.0][entry.1] = '.';
        }
        if cur == 0 {
            break
        }
        res += cur;
        cur = 0;
    }
    res
}
