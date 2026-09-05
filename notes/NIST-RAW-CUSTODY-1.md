# NIST raw archive custody lock

NON-CANONICAL. Nonformal pre-access custody only; no scientific result.
Owner: [issue #836](https://github.com/mathorn1973/twist-j/issues/836).
This implements the custody stage proposed in
[DECODER-OPEN-DATA-BRIDGE-1](DECODER-OPEN-DATA-BRIDGE-1.md).

The author has authorized examination of publicly accessible data without a
laboratory. Before any download, commit and push this complete note, the
[object list](NIST-RAW-CUSTODY-1.objects.json) and
[opaque fetcher](NIST-RAW-CUSTODY-1.fetch.py), and read back the public commit
and files. That commit is a nonformal custody lock, not a scientific probe pin.
Do not mutate its contents after acquisition begins.

Selection uses the official original-server catalogue and documentation:
the two earliest named run3 station archives and the two 00_03 synchronization
archives. Run3 has a documented unsuccessful experimental delay correction;
it is selected for record qualification, not a physical Bell test. The 00_03
archives are separate calibration records, not certified clock offsets for
run3. Published summaries are known. No payload has been opened at this lock.

The four URLs, byte counts, ETags and Last-Modified values were observed with
HTTP HEAD only. The server supplied no version ID. ETags are opaque provider
fingerprints, not claimed SHA-256 values or immutable version identifiers.
Initial custody is weaker than an independently published strong checksum.

The fetcher uses those exact URLs with If-Match and identity encoding, refuses
redirects, checks length/ETag/Last-Modified and hashes opaque bytes while
streaming. It never imports an archive library, inspects members, decompresses,
parses or previews payloads. It records only identity, byte count and SHA-256.
The destination is an untracked external cache. Existing target filenames are
refused; an interrupted acquisition is retained for audit, not overwritten or
treated as a completed receipt. The unchanged locked transfer may be retried
in a fresh directory; only complete matching objects enter the final manifest.

This note accompanies the retrieved files as their source notice. No external
data or third-party implementation is committed. The source code and apparatus
documents may be read as metadata before an analytical pin, but experimental
records and calibration payloads may not.

After opaque acquisition, a **separate complete formal pin** must contain
PREREG.md, accepted verify.py and all input/dependency hashes before the first
semantic opening. The intended bounded analysis concerns station-local raw
record prefixes, calendar metadata and sync-bracket bookkeeping; it does not
adopt physical trial completeness or a Born law. No scientific execution is
authorized by this custody lock. Canon v76 and all existing probes are unchanged.

## Source and reuse notice

Source: [NIST Bell Test Research Software and Data](https://www.nist.gov/pml/applied-physics-division/bell-test-research-software-and-data).
Catalogue: [original server archives](https://www.nist.gov/pml/applied-physics-division/bell-test-research-software-and-data/repository-bell-test-research-3).
The following is the source's notice, retained for the data copied under this
lock. The data are unmodified; new custody manifests and later analyses must
identify their date and nature. No endorsement by NIST is implied.

DISCLAIMER:

This research software and data ("belltestdata") are provided by NIST as a public service. You may use, copy and distribute copies of the software and data in any medium, provided that you keep intact this entire notice. You may improve, modify and create derivative works of the software or data or any portion of the software or data, and you may copy and distribute such modifications or works.

Modified works should carry a notice stating that you changed the software or data and should note the date and nature of any such change.

Please explicitly acknowledge the National Institute of Standards and Technology as the source of the software or data. The software/data is expressly provided "AS IS." NIST MAKES NO WARRANTY OF ANY KIND, EXPRESS, IMPLIED, IN FACT OR ARISING BY OPERATION OF LAW, INCLUDING, WITHOUT LIMITATION, THE IMPLIED WARRANTY OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NON-INFRINGEMENT AND DATA ACCURACY.

NIST NEITHER REPRESENTS NOR WARRANTS THAT THE OPERATION OF THE SOFTWARE/DATA WILL BE UNINTERRUPTED OR ERROR-FREE, OR THAT ANY DEFECTS WILL BE CORRECTED. NIST DOES NOT WARRANT OR MAKE ANY REPRESENTATIONS REGARDING THE USE OF THE SOFTWARE/DATA OR THE RESULTS THEREOF, INCLUDING BUT NOT LIMITED TO THE CORRECTNESS, ACCURACY, RELIABILITY, OR USEFULNESS OF THE SOFTWARE/DATA.

You are solely responsible for determining the appropriateness of using and distributing the software or data and you assume all risks associated with its use, including but not limited to the risks and costs of program errors, compliance with applicable laws, damage to or loss of data, programs or equipment, and the unavailability or interruption of operation.

This software or data is not intended to be used in any situation where a failure could cause risk of injury or damage to property. NIST shall not be liable for any damage that may result from errors or omissions in the software or data.

The software, data, and documentation were developed by NIST employees. NIST employee contributions are not subject to copyright protection within the United States.

Product Disclaimer

Certain trade names and company products are mentioned in the data and software to specify adequately the computer products and equipment needed to use this software. In no case does such identification imply endorsement by the National Institute of Standards and Technology of these computer products and equipment, nor does it imply that the products are necessarily the best available for the purpose.
