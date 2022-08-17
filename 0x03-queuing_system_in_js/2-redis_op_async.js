import { createClient } from 'redis';
import redis from 'redis';
import { promisify } from 'util';

const client = createClient();
client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (error) =>
  console.log(`Redis client not connected to the server: ${error.message}`)
);

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

const redisGet = promisify(client.get).bind(client);

const displaySchoolValue = async (schoolName) => {
  const res = await redisGet(schoolName);
  console.log(res);
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
