import { ApolloServer } from 'apollo-server';
import { ApolloGateway, IntrospectAndCompose } from '@apollo/gateway';

const gateway = new ApolloGateway({
  supergraphSdl: new IntrospectAndCompose({
    subgraphs: [
      { name: 'user', url: 'http://localhost:8001/graphql' },
      { name: 'role', url: 'http://localhost:8002/graphql' },
    ],
  }),
});

const server = new ApolloServer({
  gateway,
});

server.listen({ port: 4000 }).then(({ url }) => {
  console.log(`🚀 Gateway ready at ${url}`);
});
