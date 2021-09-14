# Ideas on how to do the integration

## Faasm as a new `ComputeBackend`

The first idea is to implement Faasm as a different ComputeBackend, i.e. to add
a new runtime.

Two main things need to be dechipered:
- How we send functions to Faasm
- How we send data to Faasm

Currently in Lithops:
- Function code and data are serialized (using pickle) and then sent, through a
dedicated client, to a compute backend.

Steps to integrate Lithops with Faasm:
1. Prepare a Faasm client that translates a Lithops request to a Faasm request,
   and decodes Faasm responses to Lithops responses.
2. Prepare a Faasm runtime image which can already be the worker docker image we use
   in Faasm. Faasm's worker expose an HTTP endpoint that should be enough to
   interface with the client.
3. The biggest hurdle is the way functions are written in Lithops. Python support
   in Faasm is very limited and a nightmare to maintain. I see two alternatives:
   - 3.1. We change Lithops semantics to allow calling "external functions" written
          in C/C++. I am thinking something like accepting a path as an argument to
          `map_reduce`. Then, our client (point 1) would do the Wasm compilation
          and the worker the (cached) code generation as usual. For performance,
          the Wasm compilation could also be cached in our Lithops client.
   - 3.2. We transparently support the current Lithops semantics, and try to
          cross-compile the Python function to Wasm. I have no idea how hard this
          would actually be, as Simon has been the one battling with Simon, but
          afaict it can end up very badly.
