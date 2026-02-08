use std::{collections::{HashMap, VecDeque}, fmt, fs, iter::Map, path};

enum MapObject {
    Start,
    EmptySpace,
    Splitter,
    Beam,
    Invalid
}

impl fmt::Debug for MapObject {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            MapObject::Start => write!(f, "S"),
            MapObject::EmptySpace => write!(f, "."),
            MapObject::Splitter => write!(f, "^"),
            MapObject::Beam => write!(f, "|"),
            MapObject::Invalid => write!(f, "?"),
        }
    }
}

struct State {
    splits: u64,
    beams: Vec<(usize, usize)>
}

fn print_map(map: &Vec<Vec<MapObject>>) {
    for i in 0..map.len() {
        for j in 0..map[i].len() {
            print!("{:?}", map[i][j]);
        }
        println!("");
    }

}

pub fn part1(filename: &str) -> u64 {
    let contents = fs::read_to_string(filename).expect("could not open file");

    let mut map: Vec<Vec<MapObject>> = contents.lines().map(
        |line| line.chars().filter(|ch| !ch.is_whitespace()).map(
            |char| match char {
                '.' => MapObject::EmptySpace,
                'S' => MapObject::Start,
                '^' => MapObject::Splitter,
                _ => MapObject::Invalid
            }
        ).collect()
    ).collect();

    assert!(!map.iter().flatten().any(|obj| matches!(obj, MapObject::Invalid)));

    let mut state: State = State { splits: 0, beams: vec![] };

    for i in 0..map.len() {
        for j in 0..map[i].len() {
            if matches!(map[i][j], MapObject::Start) {
                state.beams.push((i, j));
                map[i][j] = MapObject::Beam;
                break;
            }
        }
    }
    println!("state: beams: {:?}, splits: {}", state.beams, state.splits);

    while state.beams.len() > 0 {
        let mut new_beams: Vec<(usize, usize)> = vec![];
        for i in 0..state.beams.len() {
            // print_map(&map);
            let (x, y) = state.beams[i];
            if x + 1 >= map.len() {
                // done with this beam
                break;
            }
            match map[x + 1][y] {
                MapObject::EmptySpace => {
                    map[x + 1][y] = MapObject::Beam;
                    new_beams.push((x + 1, y));
                },
                MapObject::Splitter => {
                    state.splits += 1;
                    if y > 0 && !matches!(map[x + 1][y - 1], MapObject::Beam) {
                        map[x + 1][y - 1] = MapObject::Beam;
                        new_beams.push((x + 1, y - 1));
                    }
                    if y + 1 < map[x].len() && !matches!(map[x + 1][y + 1], MapObject::Beam) {
                        map[x + 1][y + 1] = MapObject::Beam;
                        new_beams.push((x + 1, y + 1));
                    }
                },
                _ => {}
            }
        }
        state.beams = new_beams;
    }

    state.splits
}

fn do_part2(x: usize, y: usize, map: &Vec<Vec<MapObject>>, cache: &mut HashMap<(usize, usize), u64>) -> u64 {
    if x + 1 >= map.len() {
        return 1;
    }

    let val = cache.get(&(x + 1, y));
    match val {
        Some(num) => { return *num; },
        None => {
            match map[x + 1][y] {
                MapObject::EmptySpace => {
                    let res = do_part2(x + 1, y, map, cache);
                    cache.insert((x + 1, y), res);
                    return res;
                },
                MapObject::Splitter => {
                    let mut res = 0;
                    if y > 0 {
                        let ans = do_part2(x + 1, y - 1, map, cache);
                        cache.insert((x + 1, y - 1), ans);
                        res += ans;
                    }
                    if y + 1 < map[x + 1].len() {
                        let ans = do_part2(x + 1, y + 1, map, cache);
                        cache.insert((x + 1, y + 1), ans);
                        res += ans;
                    }
                    return res;
                }
                _ => {
                    return 0;
                }
            }
        }
    }

}

pub fn part2(filename: &str) -> u64 {
    let contents = fs::read_to_string(filename).expect("could not open file");

    let mut map: Vec<Vec<MapObject>> = contents.lines().map(
        |line| line.chars().filter(|ch| !ch.is_whitespace()).map(
            |char| match char {
                '.' => MapObject::EmptySpace,
                'S' => MapObject::Start,
                '^' => MapObject::Splitter,
                _ => MapObject::Invalid
            }
        ).collect()
    ).collect();


    let mut x = 0;
    let mut y = 0;
    for i in 0..map.len() {
        for j in 0..map[i].len() {
            if matches!(map[i][j], MapObject::Start) {
                x = i;
                y = j;
                map[i][j] = MapObject::Beam;
            }
        }
    }
    let mut cache: HashMap<(usize, usize), u64> = HashMap::new();
    cache.insert((x, y), 1);
    return do_part2(x, y, &map, &mut cache);
}
