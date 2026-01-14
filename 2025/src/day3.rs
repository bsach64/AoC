use std::fs;

pub fn part1(filename: &str) -> i64 {
    let contents = fs::read_to_string(filename)
        .expect("could not open input file");

    let lines = contents.lines();
    let mut res = 0;

    for line in lines {
        let nums: Vec<i64> = line.chars().map(|x| x.to_string().parse().unwrap()).collect();
        let mut first_num = 0;
        let mut second_num = 0;

        for i in 0..nums.len() {
            if nums[i] > first_num && i < nums.len() - 1 {
                first_num = nums[i];
                second_num = 0;
            } else if nums[i] > second_num {
                second_num = nums[i];
            }
        }

        res += (10 * first_num) + second_num;
    }
    res
}

pub fn do_part2(nums: Vec<i64>, start: usize, left: usize) -> String {
    if left == 1 {
        let slice = &nums[start..nums.len()];
        slice.iter().max().unwrap().to_string()
    } else {
        let elem_count = nums.len() - start;
        let offset = elem_count - left + 1;
        let slice = &nums[start..start+offset];
        let max_val = slice.iter().max().unwrap_or(&0);
        let idx = slice.iter().position(|x| x == max_val).unwrap_or(0);
        // println!("slice: {:?}, start: {}, offset: {}, elem_count: {}, idx: {}, max_val: {}", slice, start, offset, elem_count, start+idx+1, max_val);
        format!("{}{}", max_val, do_part2(nums.clone(), start+idx+1, left-1))
    }
}

pub fn part2(filename: &str) -> i64 {
    // you could do something similiar to a sliding window
    // in the window arr[0:-11] (basically everything except the last 11 numbers)
    // find the largest number
    // do this again for the window i=max(arr[0:-12]) arr[i+1:-10]
    // this basically recursive algo will do the job
    // will be fun to implement ig as well

    let contents = fs::read_to_string(filename)
        .expect("could not open input file");

    let lines = contents.lines();
    let mut res: i64 = 0;

    for line in lines {
        let nums: Vec<i64> = line.chars().map(|x| x.to_string().parse().unwrap()).collect();

        let ans: i64 = do_part2(nums, 0, 12).parse().unwrap();
        res += ans;
    }
    res
}
