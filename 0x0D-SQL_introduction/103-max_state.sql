#!/usr/bin/env bash
-- displays the maximum temperature of each state
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
