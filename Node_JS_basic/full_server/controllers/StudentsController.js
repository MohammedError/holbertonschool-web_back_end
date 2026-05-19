import readDatabase from '../utils';
class StudentsController {
  static getAllStudents(request, response) {
    const dbPath = process.argv.length > 2 ? process.argv[2] : '';
    readDatabase(dbPath).then((students) => {
      const output = ['This is the list of our students'];
      const keys = Object.keys(students).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
      for (const key of keys) {
        output.push(`Number of students in ${key}: ${students[key].length}. List: ${students[key].join(', ')}`);
      }
      response.status(200).send(output.join('\n'));
    }).catch(() => {
      response.status(500).send('Cannot load the database');
    });
  }
  static getAllStudentsByMajor(request, response) {
    const field = request.params.major;
    if (field !== 'CS' && field !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    const dbPath = process.argv.length > 2 ? process.argv[2] : '';
    readDatabase(dbPath).then((students) => {
      const list = students[field] || [];
      response.status(200).send(`List: ${list.join(', ')}`);
    }).catch(() => {
      response.status(500).send('Cannot load the database');
    });
  }
}
export default StudentsController;
