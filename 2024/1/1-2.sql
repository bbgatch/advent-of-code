/*
****************************************
Advent of Code 2024: Day 1 Part 2
****************************************
*/

-- Separate ID lists
with group_1 as (
    select group_1 from 'location-ids.csv'
)
,group_2 as (
    select group_2 from 'location-ids.csv'
)

-- Join two lists. Will create duplicate records for each instance of left ID
-- in right ID list.
,count_matches as (
    select
        group_1.group_1
        ,group_2.group_2

    from group_1

        inner join group_2
            on group_1.group_1 = group_2.group_2
            
    -- where group_1.group_1 = 99781
    order by group_2
)

-- Count instances in the right list and multiply and sum for final answer
select
    group_1
    ,count(*) as count_right
    ,group_1 * count_right as multiply_by_count
    ,sum(multiply_by_count) over () as total
from count_matches
group by 1
;