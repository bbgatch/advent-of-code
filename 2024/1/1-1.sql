/*
****************************************
Advent of Code 2024: Day 1 Part 1
****************************************
*/

-- Sort 1st and 2nd ID columns 
with group_1_sort as (
    select group_1, row_number() over (order by group_1) as row_num
    from 'location-ids.csv'
)
,group_2_sort as (
    select group_2, row_number() over (order by group_2) as row_num
    from 'location-ids.csv'
)

-- Combine sorted lists using row numbers, calculate absolute difference, 
-- add up absolute differences
select
    group_1_sort.group_1
    ,group_2_sort.group_2
    ,abs(group_2_sort.group_2 - group_1_sort.group_1) as abs_diff
    ,sum(abs_diff) over () as total_abs_diff
from group_1_sort
    inner join group_2_sort
        on group_1_sort.row_num = group_2_sort.row_num
order by group_1_sort.row_num
;