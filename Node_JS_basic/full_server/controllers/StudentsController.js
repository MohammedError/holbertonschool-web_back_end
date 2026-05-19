import { readDatabase } from '../utils';

export default class StudentsController {
  static getAllStudents(request, response) {
    const dbFile = process.argv[2];

    readDatabase(dbFile)
      .then((fields) => {
        let output = 'This is the list of our students';
        const sortedFields = Object.keys(fields).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

        sortedFields.forEach((field) => {
          output += `\nNumber of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`;
        });
        return response.status(200).send(output);
      })
      .catch(() => response.status(500).send('Cannot load the database'));
  }

  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;
    const dbFile = process.argv[2];

    if (major !== 'CS' && major !== 'SWE') {
      return response.status(500).send('Major parameter must be CS or SWE');
    }

    return readDatabase(dbFile)
      .then((fields) => {
        const list = fields[major] ? fields[major].join(', ') : '';
        return response.status(200).send(`List: ${list}`);
      })
      .catch(() => response.status(500).send('Cannot load the database'));
  }
}
