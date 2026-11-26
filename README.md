# Container number claim audit

This offline static tool audits documented shipping-container-number claims against Python source calls. It examines root README prose and Markdown under docs, excluding fenced blocks; inline code counts. It normalises case, whitespace, hyphens and contractions, and removes negative matches before searching for positive matches. It never executes inspected code or contacts a network.

Install from a local distribution with `python3 -m pip install PATH`, then run:

```sh
iso6346-validation-claim-audit audit .
python3 -m iso6346_validation_claim_audit audit . --json
iso6346-validation-claim-audit --version
```

Use `--ignore PREFIX` repeatedly, `--fail-on medium` to include test-only findings in the exit threshold, and `--verbose` for the audited path. Exit status is 0 for pass, 2 for a finding at or above the threshold, and 1 for usage or I/O errors. The default threshold is high.

Positive claims without production evidence yield documented-iso6346-validation-claim-false, with medium severity when evidence exists only in tests and high otherwise. Negative claims with production evidence yield documented-no-iso6346-validation-claim-false at high severity. Evidence consists of statically recognised stdnum calls or named generic calls. Aliases are resolved and local shadows excluded. Tests count separately; fixtures, examples, docs, symlinks and syntax-invalid files do not supply production evidence. This is a heuristic, not proof that a call executes or that a claim is accurate.

## Differentiation

This audit does not cover generic input validation.
This audit does not cover ISBN book numbers.
This audit does not cover ISSN serial numbers.
This audit does not cover IBAN bank accounts.
This audit does not cover UUID strings.
This audit does not cover semantic versions.
This audit does not cover MAC addresses.
This audit does not cover BIC bank identifiers.
This audit does not cover cron expression validation.
This audit does not cover cron expression description.
This audit does not cover scheduled execution.
This audit does not cover calendar dates.
This audit does not cover timeouts.
This audit does not cover payment processing.
This audit does not cover credit card extraction.
This audit does not cover account authentication.
This audit does not cover password verification.
This audit does not cover password hashing.
This audit does not cover password generation.
This audit does not cover PDF encryption.
This audit does not cover email delivery.
This audit does not cover SMS delivery.
This audit does not cover document extraction.
This audit does not cover barcode decoding.
This audit does not cover email address validation.
This audit does not cover phone number validation.
This audit does not cover password strength.
This audit does not cover JSON Schema validation.
This audit does not cover credit card validation.
This audit does not cover domain validation.
This audit does not cover URL validation.
This audit does not cover IP address validation.
This audit does not cover JSON parsing.
This audit does not cover regular expression matching.
This audit does not cover URL parsing.
This audit does not cover web fetching.
This audit does not cover DNS lookup.
This audit does not cover barcode generation.
This audit does not cover account number extraction.
This audit does not cover vehicle number extraction.
This audit does not cover vehicle number decoding.
This audit does not cover vehicle history lookup.
This audit does not cover hex colour validation.
This audit does not cover ORCID researcher identifiers.
This audit does not cover DOI validation and resolution.
This audit does not cover CAS Registry Numbers.
This audit does not cover ISNI name identifiers.
This audit does not cover SEDOL security identifiers.
This audit does not cover ISIN security identifiers.
This audit does not cover security record lookup.
This audit does not cover security identifier extraction.
This audit does not cover IMEI identifiers.
This audit does not cover MEID identifiers.
This audit does not cover ESN identifiers.
This audit does not cover ISMN music publications.
This audit does not cover ISAN audiovisual works.
This audit does not cover GRid releases.
This audit does not cover EAN trade items.
This audit does not cover generic serial numbers.
This audit does not cover FIGI financial instruments.
This audit does not cover financial instrument lookup.
This audit does not cover financial instrument extraction.
This audit does not cover ISRC recordings.
This audit does not cover Ethereum addresses.
This audit does not cover Binance Smart Chain addresses.
This audit does not cover Tron addresses.
This audit does not cover Litecoin addresses.
This audit does not cover Dogecoin addresses.
This audit does not cover bitcoin addresses.
This audit does not cover transaction hashes.
This audit does not cover private keys.
This audit does not cover block explorer lookup.
This audit does not cover address generation.
This audit does not cover address extraction.
This audit does not cover payment receipt confirmation.
This audit does not cover spreadsheet reading.
This audit does not cover spreadsheet generation.
This audit does not cover word document reading.
This audit does not cover word document generation.
This audit does not cover presentation reading.
This audit does not cover presentation generation.
This audit does not cover PDF extraction.
This audit does not cover PDF generation.
This audit does not cover PDF merging.
This audit does not cover PDF splitting.
This audit does not cover PDF rotation.
This audit does not cover PDF form filling.
This audit does not cover PDF watermarking.
This audit does not cover PDF redaction.
This audit does not cover PDF compression.
This audit does not cover PDF annotation.
This audit does not cover table extraction.
This audit does not cover OCR.
This audit does not cover document data extraction.
This audit does not cover electronic signatures.
This audit does not cover screen recording.
This audit does not cover video generation.
This audit does not cover QR code generation.
This audit does not cover barcode scanning.
This audit does not cover audio mixing.
This audit does not cover audio generation.
This audit does not cover audio editing.
This audit does not cover audio source separation.
This audit does not cover speech recognition.
This audit does not cover text to speech.
This audit does not cover noise suppression.
This audit does not cover music generation.
This audit does not cover music transcription.
This audit does not cover InChI structures.
This audit does not cover SMILES molecular notation.
This audit does not cover EC inventory numbers.
This audit does not cover UN transport numbers.
This audit does not cover PubChem lookup.
This audit does not cover chemical structure validation.
This audit does not cover other chemical identifiers.
This audit does not cover CUSIP security identifiers.
This audit does not cover reading a container number from a shipping document.
This audit does not cover carrier registry lookup by container number.
This audit does not cover BIC registration of an owner code.
This audit does not cover container size and type codes.
This audit does not cover minting a fresh container number.

## Limitations

```
validate container number
```

The bare phrase above can denote a manual runbook step; context requires human review.

```
container number validation
```

The bare phrase above can denote a roadmap item; context requires human review.

```
container number validator
```

The bare phrase above can denote a hosted page; context requires human review.

```
container number check
```

The bare phrase above can denote a presence-only lint rule; context requires human review.

```
check container number
```

The bare phrase above can denote a manual runbook step; context requires human review.

```
verify container number
```

The bare phrase above can denote visual confirmation of a physical item; context requires human review.

```
container number verification
```

The bare phrase above can denote an external service result; context requires human review.

```
validate iso 6346
```

The bare phrase above can denote a manual runbook step; context requires human review.

```
iso 6346 validation
```

The bare phrase above can denote a specification section without code; context requires human review.

```
valid container number
```

The bare phrase above can denote example output; context requires human review.

```
container number is valid
```

The bare phrase above can denote example output; context requires human review.

```
container number is invalid
```

The bare phrase above can denote example error text; context requires human review.

```
container number validity
```

The bare phrase above can denote a configuration flag or column name; context requires human review.

```
container number format validation
```

The bare phrase above can denote a format description; context requires human review.

```
validate container number format
```

The bare phrase above can denote a format description; context requires human review.

```
check iso 6346
```

The bare phrase above can denote a checklist item; context requires human review.

```
verify iso 6346
```

The bare phrase above can denote visual confirmation of a physical item; context requires human review.

```
validate container
```

The bare phrase above can denote a Docker image check or manual runbook step; context requires human review.

```
container validation
```

The bare phrase above can denote a Docker or software packaging check; context requires human review.

```
container check
```

The bare phrase above can denote a Docker health check; context requires human review.

```
no container number validation
```

The bare phrase above can denote a roadmap item; context requires human review.

```
does not validate container number
```

The bare phrase above can denote a statement about another tool; context requires human review.

```
no container number validator
```

The bare phrase above can denote a removed dependency; context requires human review.

```
cannot validate container number
```

The bare phrase above can denote an offline mode; context requires human review.

```
no iso 6346 validation
```

The bare phrase above can denote a roadmap item; context requires human review.

```
does not validate iso 6346
```

The bare phrase above can denote a statement about another tool; context requires human review.

```
cannot validate iso 6346
```

The bare phrase above can denote an offline mode; context requires human review.

```
iso 6346
```

The bare phrase above can denote a standalone term without a validity judgement; context requires human review.

```
container
```

The bare phrase above can denote a standalone term without a validity judgement; context requires human review.

```
container number
```

The bare phrase above can denote a standalone term without a validity judgement; context requires human review.

```
owner code
```

The bare phrase above can denote a standalone term without a validity judgement; context requires human review.

```
bic
```

The bare phrase above can denote a standalone term without a validity judgement; context requires human review.

```
serial number
```

The bare phrase above can denote a standalone term without a validity judgement; context requires human review.

```
check digit
```

The bare phrase above can denote a standalone term without a validity judgement; context requires human review.

```
equipment category
```

The bare phrase above can denote a standalone term without a validity judgement; context requires human review.

A compact call only reformats its input.

A check digit calculation does not judge a complete number.

A format call only reformats its input.

An ISIN call judges a different twelve-character identifier.

A validators ISIN call judges a different identifier.

A SEDOL call judges a seven-character identifier.

A FIGI call judges a twelve-character identifier.

An ISNI call judges a sixteen-character identifier.

A CUSIP call judges a nine-character identifier.

A carrier lookup retrieves a record.

A generation call does not judge an input.

A check digit cannot catch a wrong but well-formed identifier.

The stdnum route accepts spaces and lowercase and compacts them.

Hyphens cause a length error.

Embedded tabs cause a length error.

A trailing newline is stripped.

Digits in owner-code positions are accepted.

An underscore in an owner-code position can cause an uncaught ValueError, including through the predicate.

A residue of ten maps to zero, so two residues share a digit.

Only one library route exists; validators and idutils offer no independent route.

The word container may refer to Docker or software packaging.

The library does not establish owner registration with the BIC.

The library does not establish whether a physical item exists.

A regular expression alone does not establish the checksum.

A length check alone does not establish the checksum.

A separator-position check alone does not establish the checksum.

An alphabet-only check alone does not establish the checksum.

A category-letter check alone does not establish the checksum.

An owner-code check alone does not establish the checksum.

A bare import supplies no evidence.

A string literal supplies no evidence.

A comment supplies no evidence.

A bare name reference supplies no evidence.

An external command supplies no evidence.

A roadmap item without code supplies no evidence.

A locally shadowed route supplies no evidence.

Syntax-invalid files supply no evidence.

Static analysis cannot establish whether a call runs.
