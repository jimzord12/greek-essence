# Bootstrap Dependency Map

```text
B00-01 → B00-02
B00-02 → B01-01
B01-01 → B01-02 → B01-03 → B01-04 → B01-05 → B01-06 → B01-07
B01-07 → B02-01 → B02-02 → B02-03
B02-03 → B03-01 → B03-02 → B03-03 → B03-04
B03-04 → B04-01 → B04-02 → B04-03
B04-03 → B05-01 → B05-02 → B05-03
B05-03 → B06-01 → B06-02 → B06-03
B06-03 → B07-01 → B07-02 → B07-03
```

Tasks are intentionally serialized because generators, manifests, shared configuration, and review fixes overlap. Parallel execution is allowed only when the root integrator proves that write sets do not overlap and records the deviation.

