# Changelog

## 0.4.0 (2026-05-01)

Full Changelog: [v0.3.13...v0.4.0](https://github.com/evermemos/evermemos-python/compare/v0.3.13...v0.4.0)

### Features

* **internal:** implement indices array format for query and form serialization ([460be41](https://github.com/evermemos/evermemos-python/commit/460be416108fee108d093d482207208d771b6f4b))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([9b7222d](https://github.com/evermemos/evermemos-python/commit/9b7222def8abac2970bcc4a73371e779075deb60))
* **deps:** bump minimum typing-extensions version ([d28913f](https://github.com/evermemos/evermemos-python/commit/d28913f882fc326c0996b93c347a4d39e23b681e))
* ensure file data are only sent as 1 parameter ([5a6ad09](https://github.com/evermemos/evermemos-python/commit/5a6ad09a54d7fd0e6d805c86eb12246cef469863))
* **pydantic:** do not pass `by_alias` unless set ([9786776](https://github.com/evermemos/evermemos-python/commit/97867769c90346476b205f8e42fdef295f712b0b))
* sanitize endpoint path params ([5a8377f](https://github.com/evermemos/evermemos-python/commit/5a8377f2b2c6620ae4baf3cd091638cac1116a78))


### Chores

* **ci:** bump uv version ([da041d5](https://github.com/evermemos/evermemos-python/commit/da041d5677f9cd0273554515329c8aad11ee8e46))
* **ci:** skip lint on metadata-only changes ([5c190ea](https://github.com/evermemos/evermemos-python/commit/5c190ea3b710d4d5074cac810ed4920609512ce0))
* **ci:** skip uploading artifacts on stainless-internal branches ([721abc8](https://github.com/evermemos/evermemos-python/commit/721abc8a7ae2a386bbadc0b55e5e5caab1211759))
* **internal:** add request options to SSE classes ([3d9a5d8](https://github.com/evermemos/evermemos-python/commit/3d9a5d842819e938a9b91e2228caa5820e5f8ab4))
* **internal:** codegen related update ([118d6b1](https://github.com/evermemos/evermemos-python/commit/118d6b152673d3e583cfc6baa9b7aefe51e95e01))
* **internal:** codegen related update ([67e0217](https://github.com/evermemos/evermemos-python/commit/67e02174360ef983ab9b9d2e3e030b7d0f3fa75e))
* **internal:** codegen related update ([4af43ee](https://github.com/evermemos/evermemos-python/commit/4af43ee961f0dda38a7391607776558c5996e858))
* **internal:** codegen related update ([b743f30](https://github.com/evermemos/evermemos-python/commit/b743f30bc21a2adc20b80eaa3bf7a36e448481df))
* **internal:** make `test_proxy_environment_variables` more resilient ([b75db1c](https://github.com/evermemos/evermemos-python/commit/b75db1cf66897f85bb4e96b0c2fe37649ec4c7ef))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([e90baf7](https://github.com/evermemos/evermemos-python/commit/e90baf7a239546f50667af8d67aaf80bba256e5f))
* **internal:** remove mock server code ([fcbe761](https://github.com/evermemos/evermemos-python/commit/fcbe7615195686bb09fcbf3fda208d954fe9daaa))
* **internal:** tweak CI branches ([ff8dcc9](https://github.com/evermemos/evermemos-python/commit/ff8dcc9ea080079828a0323df7265b5776bc625d))
* **internal:** update gitignore ([c4581ec](https://github.com/evermemos/evermemos-python/commit/c4581ec2c38d0bc62b4e9a522599c483788376d7))
* update mock server docs ([f09c77f](https://github.com/evermemos/evermemos-python/commit/f09c77f977f05ac11659589785538c7566e1eeca))

## 0.3.13 (2026-02-13)

Full Changelog: [v0.3.12...v0.3.13](https://github.com/evermemos/evermemos-python/compare/v0.3.12...v0.3.13)

### Features

* **api:** api update ([3e2055c](https://github.com/evermemos/evermemos-python/commit/3e2055c7c7264f7192e147cba95ff8a4b00c3e6c))


### Chores

* format all `api.md` files ([334f048](https://github.com/evermemos/evermemos-python/commit/334f0482a42ba7aa443da7f76da45d4d75b56e77))
* **internal:** fix lint error on Python 3.14 ([7025e9a](https://github.com/evermemos/evermemos-python/commit/7025e9ab9c47bde3f1add8a522b69d22cd73af32))

## 0.3.12 (2026-02-11)

Full Changelog: [v0.3.11...v0.3.12](https://github.com/evermemos/evermemos-python/compare/v0.3.11...v0.3.12)

### Features

* **api:** api update ([6474a06](https://github.com/evermemos/evermemos-python/commit/6474a06e99093960ffecfdb8fc8bc932c677dc7c))


### Chores

* **internal:** bump dependencies ([dd71dc0](https://github.com/evermemos/evermemos-python/commit/dd71dc09c0b401fc21435919e5084cb160bcc274))

## 0.3.11 (2026-02-06)

Full Changelog: [v0.4.0...v0.3.11](https://github.com/evermemos/evermemos-python/compare/v0.4.0...v0.3.11)

### Features

* **api:** api update ([ddfdd8c](https://github.com/evermemos/evermemos-python/commit/ddfdd8c03ce83031ddadf78d5c99a60e2a640c91))
* **api:** api update ([0981f02](https://github.com/evermemos/evermemos-python/commit/0981f021d776d39cb9278f8ced62d749459fd613))
* **api:** api update ([98f0599](https://github.com/evermemos/evermemos-python/commit/98f05990549d226b03aa4a006b994df14ca91967))
* **api:** api update ([9cef371](https://github.com/evermemos/evermemos-python/commit/9cef37158fce900009a56362b9c9b962084be202))
* **api:** api update ([e2cc79c](https://github.com/evermemos/evermemos-python/commit/e2cc79c7b19cd8da12385d59bd6fcb7e83be6c84))
* **api:** api update ([b5a5ad3](https://github.com/evermemos/evermemos-python/commit/b5a5ad30160d7b74918456a269d2be73feb173ba))
* **api:** api update ([ff8658d](https://github.com/evermemos/evermemos-python/commit/ff8658dbfa447af49ad0bf42ddf3a7bf84c5af08))
* **api:** api update ([c401fd7](https://github.com/evermemos/evermemos-python/commit/c401fd730329f8dd4b35925b9cf58cd90557dd4c))
* **api:** api update ([7e45e6a](https://github.com/evermemos/evermemos-python/commit/7e45e6ae832e94bd98c4e45abad5cdc555448e37))
* **client:** add custom JSON encoder for extended type support ([07e2cfe](https://github.com/evermemos/evermemos-python/commit/07e2cfe00b6360c7227fa0149c8aaf8697d3ec3f))


### Bug Fixes

* updates version to v0.3.5 ([26dd42f](https://github.com/evermemos/evermemos-python/commit/26dd42fa94230ddd0762731d98713c0b4e031e91))
* updates version to v0.3.6 ([d2c9c91](https://github.com/evermemos/evermemos-python/commit/d2c9c91ecd826067e245c8c7aafb3445a8e5fdca))


### Chores

* sync repo ([492f867](https://github.com/evermemos/evermemos-python/commit/492f8671ad8664e7153da413aac24d37575339bc))
* update SDK settings ([135157a](https://github.com/evermemos/evermemos-python/commit/135157adbfe192a90a78aa0c51418a764649d054))
* update SDK settings ([d6a254c](https://github.com/evermemos/evermemos-python/commit/d6a254c0c35bc5e1a0a74bb5c5f8b7d96f1c92e1))
* update SDK settings ([dda1b57](https://github.com/evermemos/evermemos-python/commit/dda1b5786d59336c1ace3363876de645fcffccb7))
* update SDK settings ([7ea187d](https://github.com/evermemos/evermemos-python/commit/7ea187dd45a43f915258b17cd9d98b2e8624f948))
* update SDK settings ([f727a84](https://github.com/evermemos/evermemos-python/commit/f727a84dbc4e5cb8a04adfa14ce79f6254f54ead))
* update SDK settings ([c6d796d](https://github.com/evermemos/evermemos-python/commit/c6d796d7bbbec539954c1802094932a919d0b8e5))
* update SDK settings ([11a1c09](https://github.com/evermemos/evermemos-python/commit/11a1c09da854becb6567ad5428db716e38e81ee0))
* update SDK settings ([7846bc7](https://github.com/evermemos/evermemos-python/commit/7846bc750ca4ab190a39feeb9dfd096854618cb1))
* update SDK settings ([fa846b9](https://github.com/evermemos/evermemos-python/commit/fa846b9647c78fbd9b072b6d397b8c74bbdfa2d4))
* update SDK settings ([aeeff07](https://github.com/evermemos/evermemos-python/commit/aeeff070828972d2e554cb3a0037d71ee1b7e795))
* update SDK settings ([691323b](https://github.com/evermemos/evermemos-python/commit/691323ba6b690b4572eeb1a2f2a65f834d4bc70e))
* update SDK settings ([6080ec3](https://github.com/evermemos/evermemos-python/commit/6080ec350c2aeed1448824b2aea863e80d17e6cf))
* update SDK settings ([14b82aa](https://github.com/evermemos/evermemos-python/commit/14b82aad0c71e9fa6b5513762769de826aa739dc))
* update SDK settings ([9c6197a](https://github.com/evermemos/evermemos-python/commit/9c6197a694d6d3bc52d1728c2fd0d507e993d627))
* update SDK settings ([aa51d08](https://github.com/evermemos/evermemos-python/commit/aa51d085e5b2569944c78cbd4a39fbb2218a47f5))
* updates version to v0.3.3 ([f84f905](https://github.com/evermemos/evermemos-python/commit/f84f9056ffb360af552138ccc9650766c98f79e6))

## 0.4.0 (2026-02-06)

Full Changelog: [v0.3.10...v0.4.0](https://github.com/evermemos/evermemos-python/compare/v0.3.10...v0.4.0)

### Features

* **api:** api update ([ddfdd8c](https://github.com/evermemos/evermemos-python/commit/ddfdd8c03ce83031ddadf78d5c99a60e2a640c91))
* **api:** api update ([0981f02](https://github.com/evermemos/evermemos-python/commit/0981f021d776d39cb9278f8ced62d749459fd613))

## 0.3.10 (2026-01-31)

Full Changelog: [v0.3.9...v0.3.10](https://github.com/evermemos/evermemos-python/compare/v0.3.9...v0.3.10)

### Features

* **api:** api update ([98f0599](https://github.com/evermemos/evermemos-python/commit/98f05990549d226b03aa4a006b994df14ca91967))
* **client:** add custom JSON encoder for extended type support ([07e2cfe](https://github.com/evermemos/evermemos-python/commit/07e2cfe00b6360c7227fa0149c8aaf8697d3ec3f))


### Chores

* update SDK settings ([135157a](https://github.com/evermemos/evermemos-python/commit/135157adbfe192a90a78aa0c51418a764649d054))
* update SDK settings ([d6a254c](https://github.com/evermemos/evermemos-python/commit/d6a254c0c35bc5e1a0a74bb5c5f8b7d96f1c92e1))
* update SDK settings ([dda1b57](https://github.com/evermemos/evermemos-python/commit/dda1b5786d59336c1ace3363876de645fcffccb7))

## 0.3.9 (2026-01-29)

Full Changelog: [v0.3.8...v0.3.9](https://github.com/evermemos/evermemos-python/compare/v0.3.8...v0.3.9)

### Features

* **api:** api update ([9cef371](https://github.com/evermemos/evermemos-python/commit/9cef37158fce900009a56362b9c9b962084be202))


### Chores

* update SDK settings ([7ea187d](https://github.com/evermemos/evermemos-python/commit/7ea187dd45a43f915258b17cd9d98b2e8624f948))
* update SDK settings ([f727a84](https://github.com/evermemos/evermemos-python/commit/f727a84dbc4e5cb8a04adfa14ce79f6254f54ead))

## 0.3.8 (2026-01-28)

Full Changelog: [v0.3.7...v0.3.8](https://github.com/evermemos/evermemos-python/compare/v0.3.7...v0.3.8)

### Features

* **api:** api update ([e2cc79c](https://github.com/evermemos/evermemos-python/commit/e2cc79c7b19cd8da12385d59bd6fcb7e83be6c84))


### Chores

* update SDK settings ([c6d796d](https://github.com/evermemos/evermemos-python/commit/c6d796d7bbbec539954c1802094932a919d0b8e5))
* update SDK settings ([11a1c09](https://github.com/evermemos/evermemos-python/commit/11a1c09da854becb6567ad5428db716e38e81ee0))

## 0.3.7 (2026-01-27)

Full Changelog: [v0.3.6...v0.3.7](https://github.com/evermemos/evermemos-python/compare/v0.3.6...v0.3.7)

### Features

* **api:** api update ([b5a5ad3](https://github.com/evermemos/evermemos-python/commit/b5a5ad30160d7b74918456a269d2be73feb173ba))
* **api:** api update ([ff8658d](https://github.com/evermemos/evermemos-python/commit/ff8658dbfa447af49ad0bf42ddf3a7bf84c5af08))


### Chores

* update SDK settings ([7846bc7](https://github.com/evermemos/evermemos-python/commit/7846bc750ca4ab190a39feeb9dfd096854618cb1))
* update SDK settings ([fa846b9](https://github.com/evermemos/evermemos-python/commit/fa846b9647c78fbd9b072b6d397b8c74bbdfa2d4))

## 0.3.6 (2026-01-26)

Full Changelog: [v0.3.6...v0.3.6](https://github.com/evermemos/evermemos-python/compare/v0.3.6...v0.3.6)

### Features

* **api:** api update ([c401fd7](https://github.com/evermemos/evermemos-python/commit/c401fd730329f8dd4b35925b9cf58cd90557dd4c))
* **api:** api update ([7e45e6a](https://github.com/evermemos/evermemos-python/commit/7e45e6ae832e94bd98c4e45abad5cdc555448e37))


### Bug Fixes

* updates version to v0.3.5 ([26dd42f](https://github.com/evermemos/evermemos-python/commit/26dd42fa94230ddd0762731d98713c0b4e031e91))
* updates version to v0.3.6 ([d2c9c91](https://github.com/evermemos/evermemos-python/commit/d2c9c91ecd826067e245c8c7aafb3445a8e5fdca))


### Chores

* sync repo ([492f867](https://github.com/evermemos/evermemos-python/commit/492f8671ad8664e7153da413aac24d37575339bc))
* update SDK settings ([aeeff07](https://github.com/evermemos/evermemos-python/commit/aeeff070828972d2e554cb3a0037d71ee1b7e795))
* update SDK settings ([691323b](https://github.com/evermemos/evermemos-python/commit/691323ba6b690b4572eeb1a2f2a65f834d4bc70e))
* update SDK settings ([6080ec3](https://github.com/evermemos/evermemos-python/commit/6080ec350c2aeed1448824b2aea863e80d17e6cf))
* update SDK settings ([14b82aa](https://github.com/evermemos/evermemos-python/commit/14b82aad0c71e9fa6b5513762769de826aa739dc))
* update SDK settings ([9c6197a](https://github.com/evermemos/evermemos-python/commit/9c6197a694d6d3bc52d1728c2fd0d507e993d627))
* update SDK settings ([aa51d08](https://github.com/evermemos/evermemos-python/commit/aa51d085e5b2569944c78cbd4a39fbb2218a47f5))
* updates version to v0.3.3 ([f84f905](https://github.com/evermemos/evermemos-python/commit/f84f9056ffb360af552138ccc9650766c98f79e6))

## 0.3.5 (2026-01-26)

Full Changelog: [v0.3.5...v0.3.5](https://github.com/evermemos/evermemos-python/compare/v0.3.5...v0.3.5)

### Features

* **api:** api update ([c401fd7](https://github.com/evermemos/evermemos-python/commit/c401fd730329f8dd4b35925b9cf58cd90557dd4c))
* **api:** api update ([7e45e6a](https://github.com/evermemos/evermemos-python/commit/7e45e6ae832e94bd98c4e45abad5cdc555448e37))


### Bug Fixes

* updates version to v0.3.5 ([26dd42f](https://github.com/evermemos/evermemos-python/commit/26dd42fa94230ddd0762731d98713c0b4e031e91))


### Chores

* sync repo ([492f867](https://github.com/evermemos/evermemos-python/commit/492f8671ad8664e7153da413aac24d37575339bc))
* update SDK settings ([aeeff07](https://github.com/evermemos/evermemos-python/commit/aeeff070828972d2e554cb3a0037d71ee1b7e795))
* update SDK settings ([691323b](https://github.com/evermemos/evermemos-python/commit/691323ba6b690b4572eeb1a2f2a65f834d4bc70e))
* update SDK settings ([6080ec3](https://github.com/evermemos/evermemos-python/commit/6080ec350c2aeed1448824b2aea863e80d17e6cf))
* update SDK settings ([14b82aa](https://github.com/evermemos/evermemos-python/commit/14b82aad0c71e9fa6b5513762769de826aa739dc))
* update SDK settings ([9c6197a](https://github.com/evermemos/evermemos-python/commit/9c6197a694d6d3bc52d1728c2fd0d507e993d627))
* update SDK settings ([aa51d08](https://github.com/evermemos/evermemos-python/commit/aa51d085e5b2569944c78cbd4a39fbb2218a47f5))
* updates version to v0.3.3 ([f84f905](https://github.com/evermemos/evermemos-python/commit/f84f9056ffb360af552138ccc9650766c98f79e6))

## 0.3.4 (2026-01-26)

Full Changelog: [v0.4.0...v0.3.4](https://github.com/evermemos/evermemos-python/compare/v0.4.0...v0.3.4)

### Features

* **api:** api update ([7e45e6a](https://github.com/evermemos/evermemos-python/commit/7e45e6ae832e94bd98c4e45abad5cdc555448e37))


### Chores

* sync repo ([492f867](https://github.com/evermemos/evermemos-python/commit/492f8671ad8664e7153da413aac24d37575339bc))
* update SDK settings ([6080ec3](https://github.com/evermemos/evermemos-python/commit/6080ec350c2aeed1448824b2aea863e80d17e6cf))
* update SDK settings ([14b82aa](https://github.com/evermemos/evermemos-python/commit/14b82aad0c71e9fa6b5513762769de826aa739dc))
* update SDK settings ([9c6197a](https://github.com/evermemos/evermemos-python/commit/9c6197a694d6d3bc52d1728c2fd0d507e993d627))
* update SDK settings ([aa51d08](https://github.com/evermemos/evermemos-python/commit/aa51d085e5b2569944c78cbd4a39fbb2218a47f5))
* updates version to v0.3.3 ([f84f905](https://github.com/evermemos/evermemos-python/commit/f84f9056ffb360af552138ccc9650766c98f79e6))

## 0.4.0 (2026-01-26)

Full Changelog: [v0.3.3...v0.4.0](https://github.com/evermemos/evermemos-python/compare/v0.3.3...v0.4.0)

### Features

* **api:** api update ([7e45e6a](https://github.com/evermemos/evermemos-python/commit/7e45e6ae832e94bd98c4e45abad5cdc555448e37))


### Chores

* sync repo ([492f867](https://github.com/evermemos/evermemos-python/commit/492f8671ad8664e7153da413aac24d37575339bc))
* update SDK settings ([6080ec3](https://github.com/evermemos/evermemos-python/commit/6080ec350c2aeed1448824b2aea863e80d17e6cf))
* update SDK settings ([14b82aa](https://github.com/evermemos/evermemos-python/commit/14b82aad0c71e9fa6b5513762769de826aa739dc))
* update SDK settings ([9c6197a](https://github.com/evermemos/evermemos-python/commit/9c6197a694d6d3bc52d1728c2fd0d507e993d627))
* update SDK settings ([aa51d08](https://github.com/evermemos/evermemos-python/commit/aa51d085e5b2569944c78cbd4a39fbb2218a47f5))
* updates version to v0.3.3 ([f84f905](https://github.com/evermemos/evermemos-python/commit/f84f9056ffb360af552138ccc9650766c98f79e6))

## 0.3.2 (2026-01-26)

Full Changelog: [v0.3.2...v0.3.2](https://github.com/evermemos/evermemos-python/compare/v0.3.2...v0.3.2)

### Features

* **api:** api update ([7e45e6a](https://github.com/evermemos/evermemos-python/commit/7e45e6ae832e94bd98c4e45abad5cdc555448e37))


### Chores

* sync repo ([492f867](https://github.com/evermemos/evermemos-python/commit/492f8671ad8664e7153da413aac24d37575339bc))
* update SDK settings ([6080ec3](https://github.com/evermemos/evermemos-python/commit/6080ec350c2aeed1448824b2aea863e80d17e6cf))
* update SDK settings ([14b82aa](https://github.com/evermemos/evermemos-python/commit/14b82aad0c71e9fa6b5513762769de826aa739dc))
* update SDK settings ([9c6197a](https://github.com/evermemos/evermemos-python/commit/9c6197a694d6d3bc52d1728c2fd0d507e993d627))
* update SDK settings ([aa51d08](https://github.com/evermemos/evermemos-python/commit/aa51d085e5b2569944c78cbd4a39fbb2218a47f5))

## 0.1.2 (2026-01-26)

Full Changelog: [v0.1.1...v0.1.2](https://github.com/evermemos/evermemos-python/compare/v0.1.1...v0.1.2)

## 0.1.1 (2026-01-26)

Full Changelog: [v0.1.0...v0.1.1](https://github.com/evermemos/evermemos-python/compare/v0.1.0...v0.1.1)

## 0.1.0 (2026-01-26)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/evermemos/evermemos-python/compare/v0.0.1...v0.1.0)

### Features

* **api:** api update ([7e45e6a](https://github.com/evermemos/evermemos-python/commit/7e45e6ae832e94bd98c4e45abad5cdc555448e37))


### Chores

* sync repo ([492f867](https://github.com/evermemos/evermemos-python/commit/492f8671ad8664e7153da413aac24d37575339bc))
* update SDK settings ([6080ec3](https://github.com/evermemos/evermemos-python/commit/6080ec350c2aeed1448824b2aea863e80d17e6cf))
* update SDK settings ([14b82aa](https://github.com/evermemos/evermemos-python/commit/14b82aad0c71e9fa6b5513762769de826aa739dc))
* update SDK settings ([9c6197a](https://github.com/evermemos/evermemos-python/commit/9c6197a694d6d3bc52d1728c2fd0d507e993d627))
* update SDK settings ([aa51d08](https://github.com/evermemos/evermemos-python/commit/aa51d085e5b2569944c78cbd4a39fbb2218a47f5))
