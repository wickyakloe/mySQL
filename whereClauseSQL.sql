/*
Select all `Track` records where the `Composer` is `U2`
*/
select * from Track
where Composer = 'U2';

/*
Select all `Album` records where the `AlbumId` is 232;
*/
select * from Album
where AlbumId = 232;

/*
Select the `FirstName`, `LastName` and `Title` for every
`Employee` that has a `Title` of "IT Staff"
*/
select FirstName, LastName, Title from Employee
where Title = 'IT Staff';