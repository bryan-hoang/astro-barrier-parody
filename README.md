# Astro Barrier Parody

[![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

A parody of the [Astro Barrier][astro-barrier-wiki] game from Club Penguin
created during the 2018 [Major League Hacking (MLH)][mlh] Local Hack Day.

[mlh]: https://mlh.io/about
[astro-barrier-wiki]: https://clubpenguin.fandom.com/wiki/Astro_Barrier

The game consists of one simple level where the player uses the left and right
arrow keys to move a ship and spacebar to shoot bullets at a moving target. The
player has an ammo limit of 10 bullets with an additional constraint of a timer.
Once either resource runs out before all of the targets are hit, 'Game Over'
text pops up. Else, you win and can restart the game back at the start screen.

Built with [The Python Arcade Library][arcade].

[arcade]: https://github.com/pythonarcade/arcade

## Install

Prerequisites:

- [uv](https://docs.astral.sh/uv/getting-started/installation/)

Steps:

```console
git clone https://github.com/bryan-hoang/astro-barrier-parody.git
cd astro-barrier-parody
uv sync
```

## Usage

```console
uv run poe game
```

## Maintainers

- [@bryan-hoang](https://github.com/bryan-hoang)
- [@liam-cregg](https://github.com/liam-cregg)
- [@edendabreo](https://github.com/edendabreo)

## Contributing

PRs accepted.

Small note: If editing the README, please conform to the
[standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

MIT © 2018 Bryan Hoang and contributors
