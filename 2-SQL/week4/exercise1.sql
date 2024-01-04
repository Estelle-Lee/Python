select * from moma_works
where classification='Photograph';

select height, width from moma_works
where classification='Photograph' AND height >0 AND width>0;

select
ceil(width)+2 as frame_width,
ceil(height)+4 as frame_height
from moma_works
where classification='Photograph' AND height >0 AND width>0;

WITH frames AS (
	SELECT 
	ceil(width)+2 as frame_width,
	ceil(height)+4 as frame_height
	from moma_works
	where classification='Photograph' AND height >0 AND width>0
)
SELECT
frame_width,
frame_height,
frame_width* frame_height as frame_area
from frames;


WITH frames AS (
	SELECT 
	ceil(width)+2 as frame_width,
	ceil(height)+4 as frame_height
	from moma_works
	where classification='Photograph' AND height >0 AND width>0
)
SELECT
count(*),
frame_width,
frame_height,
frame_width* frame_height as frame_area
from frames
group by frame_width, frame_height, frame_area;