import fs from 'fs';

const readDatabase = (filePath) => new Promise((resolve, reject) => {
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      reject(err);
      return;
    }
    const lines = data.trim().split('\n');
    const students = lines.slice(1);
    const fields = {};
    students.forEach((student) => {
      if (student) {
        const studentData = student.split(',');
        const firstName = studentData[0];
        const field = studentData[3];
        if (!fields[field]) fields[field] = [];
        fields[field].push(firstName);
      }
    });
    resolve(fields);
  });
});

export default readDatabase;
