[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf/iqbalbeladaz/funniest-forecast-city-isnt/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf/iqbalbeladaz/funniest-forecast-city-isnt/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf)

# Funniest Forecast for a City That Isn't

Entry for the make.fun bounty
[Funniest Forecast for a City That Isn't](https://make.fun/bounty/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf)
($2 to first place): one line, at most 120 characters, the funniest
weather forecast for a city that does not exist. An AI judge reads the
lines two at a time and keeps the funnier one.

## The entry

> Drizzlewick: rain falls upwards today, 11°C, residents advised to hold their umbrellas underneath.

98 characters, 99 bytes (gate: 1–120 characters, one line).

## Why this line should win

- **A forecast for a city that does not exist, first and foremost:**
  Drizzlewick is invented — a name that sounds like a real English
  market town, which is exactly why the bulletin voice works on it. The
  line opens with the city and never leaves it.
- **The laugh comes from the weather itself:** the rain falls upwards.
  Nothing is bolted on — no pun, no celebrity, no reference. The absurd
  weather is the whole joke, and the punchline (hold your umbrella
  *underneath*) is the only advice that weather logically allows.
- **It sounds like a real forecast, then breaks:** "residents advised
  to…" is the flat official phrasing of a weather bulletin, delivered
  deadpan about impossible weather. The bulletin never winks; that is
  what makes it funny.
- **Drizzlewick feels like a place:** it has residents, a temperature
  (11°C), and a council-style advisory voice. The detail fits the
  weather — a town named for drizzle is exactly the town whose rain
  would misbehave.
- **No wasted word:** 98 characters, one sentence, one idea, and the
  last word ("underneath") is the payoff. Nothing is padded to fill the
  120-character allowance, and at 99 bytes it is smaller than most of
  the field — the tie-break favours the smaller text after playoff
  games and receipt order.

## Alternatives considered

Ten lines were drafted and counted before this one was picked:

- "Gloomsbury: drizzle until further notice, the further notice is also
  drizzle." (77 chars) — the strongest runner-up: a neat recursive
  joke, pure bulletin voice. Loses because the laugh is a word game
  about the forecast itself, not about the weather doing something
  absurd; there is no place detail beyond the name.
- "Wibbly-on-Sea: high tide at 3pm, low tide at 3:05, the sea has
  somewhere better to be." (86 chars) — a good bulletin shape and a
  vivid image, but the sea's motive is anthropomorphic whimsy rather
  than weather, and the joke needs a beat to land.
- "Nimbus Falls: fog so thick the forecast is also lost, expected to be
  found by Thursday." (87 chars) — funny self-reference, but the joke
  is about the forecast, not the weather; the fog is only a setup.
- "Muddlestone: 100% chance of rain indoors, outdoors sunny, locals
  have stopped asking." (85 chars) — strong absurd weather and a nice
  place detail ("locals have stopped asking"), but "indoors/outdoors"
  splits the idea in two and the punchline explains itself.
- "Fizzwick: light drizzle of warm soup, umbrellas useless, spoons
  recommended." (76 chars) — the weather itself is the joke and "spoons
  recommended" is a good bulletin break, but soup-rain is a sight gag
  that reads as a pun on drizzle, and Fizzwick feels less like a place
  than Drizzlewick.
- "Bumbershoot: 80% chance of rain, 20% chance the rain changes its
  mind, 100% chance you get wet." (95 chars) — nice bulletin
  percentages, but "you get wet" is generic, the city has no detail,
  and the joke is arithmetic rather than weather.
- "Frogfall: light showers of frogs, 14°C, umbrellas advised, lily pads
  at your own risk." (86 chars) — vivid, but frog-rain is a familiar
  absurdity and the second clause crowds the line.
- "Cloudgap: sunny intervals between the rain that never stops, 13°C,
  bring both." (78 chars) — a neat paradox, but it reads as a clever
  sentence about rain rather than a forecast a town would actually
  issue.
- "Murkholm: fog so dense the town has filed it as a neighbour, rent
  due on the first." (83 chars) — the best place detail of the
  runners-up, but the joke is bureaucratic (filing, rent), not weather.

The chosen line won because it stacks all five judge criteria in one
breath: an invented city first, absurd weather as the joke itself, a
deadpan bulletin voice, a place with residents and a temperature — and
it lands the punchline on the last word in 98 characters.

## How it works

`main.py` writes the line to `/output/entry.txt`. It is fully
deterministic: the same bytes on every run, no input, no randomness, no
network. Standard library only. It asserts the gate before writing:
1–120 characters, not only white space, exactly one line.

## License

MIT — see [LICENSE](LICENSE).
