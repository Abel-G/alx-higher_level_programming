#!/usr/bin/env bash
-- creates the table unique_id
CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1,
    name VARCHAR(256));