export default function createIteratorObject(report) {
  const allEmployees = [];
  for (const dept of Object.values(report.allEmployees)) {
    allEmployees.push(...dept);
  }
  return allEmployees;
}
