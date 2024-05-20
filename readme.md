# F1 2024 Race Schedule CSV Generator

This Python script fetches the upcoming F1 2024 race schedule from the Ergast API and generates two separate CSV files: one for normal races and another for sprint races. The CSV files include detailed session timings in UK timezone.

## Features

- Fetches F1 2024 race schedule from the Ergast API.
- Generates two CSV files:
  - `f1_2024_normal_race_schedule.csv` for normal races.
  - `f1_2024_sprint_race_schedule.csv` for sprint races.
- Converts all session times to UK timezone.

## Normal Race CSV Format

The `f1_2024_normal_race_schedule.csv` includes the following columns:

- Race Name
- Country
- FP1 and FP2 Date
- FP1 Time
- FP2 Time
- FP3 and Quali Date
- FP3 Time
- Quali Time
- Race Date
- Race Time

## Sprint Race CSV Format

The `f1_2024_sprint_race_schedule.csv` includes the following columns:

- Race Name
- Country
- FP1 & Sprint Quali Date
- FP1 Time
- Sprint Quali Date
- Sprint Quali Time
- Sprint & Quali Date
- Sprint Time
- Quali Time
- Race Date
- Race Time
