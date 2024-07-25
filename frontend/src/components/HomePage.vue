<template>
  <div class="welcome">
    <h1>Python</h1>
    <br /><br />
    <p class="intro">
      Python is a versatile programming language that is widely used in the
      software development industry. This course will introduce you to the
      fundamentals of Python programming and provide you with the skills to
      design and develop Python applications.
    </p>
    <hr class="separator" />
    <br /><br />
    <ul class="outcomes">
      <li>
        Course Outcome 1: Understand and apply fundamental programming concepts
        in Python, including variables, data types, and control structures.
      </li>
      <li>
        Course Outcome 2: Develop proficiency in using Python libraries for data
        manipulation, such as NumPy and pandas.
      </li>
      <li>
        Course Outcome 3: Design and implement functions and modules to create
        modular and reusable code.
      </li>
      <li>
        Course Outcome 4: Utilize object-oriented programming principles to
        design and develop Python applications.
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "HomePage",
};
</script>

<style scoped>
.welcome h1 {
  text-align: center;
  margin-top: 25px;
}
.welcome .intro {
  text-align: center;
  width: 50%; /* Adjust this value to change the width of the paragraph */
  margin: 0 auto; /* This will center the paragraph */
}
.outcomes {
  margin-left: 50px;
}
.outcomes li {
  margin-bottom: 10px;
}
.separator {
  margin: 20px auto;
  width: 50%; /* Adjust the width of the line */
  border-top: 1px solid #000; /* Change the color and style as needed */
}
</style>
