select genre, count(*) from books
group by genre;

select genre, count(*) from books
group by genre
having count(*)>1;