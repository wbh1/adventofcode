# Advent of Code 2023-

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

I use pytest for validating that my solution matches the expected output from the sample data in each problem. To run a test:

```console
❯ uv run pytest adventofcode/2023/test_day1.py
```
