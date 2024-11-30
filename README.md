# Advent of Code 2023-????

I'm using Python because I don't have the time to use Go :(

## Usage

I rely on [uv](https://docs.astral.sh/uv) for my Python projects. Consequently, I use the `aoc.py` script to run solutions like so:

```sh
uv run aoc.py -y 2023 1
```

## Inputs

Inputs are [SOPS](https://getsops.io/docs/#encrypting-using-age)-encrypted using `age`. To decrypt/encrypt files, I use tasks from [mise](https://mise.jdx.dev/tasks/running-tasks.html). They're documented below:

### `input`

- Depends: input:*

- **Usage**: `mise run input`

Encrypt and decrypt all input files

### `input:decrypt`

- **Usage**: `mise run input:decrypt`

Decrypt all secret files

### `input:encrypt`

- **Usage**: `mise run input:encrypt`

Encrypt all non-secret files

## Testing

I use pytest for validating that my solution matches the expected output from the sample data in each problem. To run a test using a task defined in `mise`:

```console
❯ mise run test --year 2023 1
```

## Prior Years

I'm trying to use just 1 repo going forward since I found a structure that works for me and is re-usable across years.

My prior years are available in other repos:

- [2018](https://github.com/wbh1/advent-of-code2018)
- [2019](https://github.com/wbh1/adventofcode2019)
- [2020](https://github.com/wbh1/adventofcode2020)
- [2021](https://github.com/wbh1/adventofcode2021)
- [2022](https://github.com/wbh2/adventofcode2022)
