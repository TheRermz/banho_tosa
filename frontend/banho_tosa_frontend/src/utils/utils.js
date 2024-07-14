const formatDate = (dateInSeconds) => {
  const formattedDate = new Date(dateInSeconds * 1000);
  const day = formattedDate.getDate().toString().padStart(2, "0");
  const month = (formattedDate.getMonth() + 1).toString().padStart(2, "0");
  const year = formattedDate.getFullYear().toString();

  return `${day}/${month}/${year}`;
};

// Example usage:
const apiDateInSeconds = 1660588800; // Replace with the date received from the API in seconds
const formattedDate = formatDate(apiDateInSeconds);
console.log(formattedDate); // Output: 14/08/2022
