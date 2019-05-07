update salary
set sex = CASE
WHEN sex = 'm' then 'f'
WHEN sex = 'f' then 'm'
END;
