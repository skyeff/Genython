# Genython

## Synopsis

**Genython** constitutes a streamlined computational framework for genomic
sequence manipulation and analysis, engineered as a pedagogical distillate of
BioPython's architectural principles. This implementation privileges clarity
over comprehensiveness, furnishing essential primitives for nucleotide
interrogation, transcriptional simulation, and proteomic translation.

## Architectural Philosophy

The design eschews monolithic dependency chains in favor of algorithmic
transparency. Each method operates as a self-contained transformation kernel,
exposing the molecular logic underlying genetic information processing. Where
industrial frameworks prioritize feature saturation, Genython crystallizes
foundational operations into legible, extensible components.

## Core Capabilities

### Sequence Acquisition & Preprocessing
- **FASTA ingestion** with automatic header excision
- **Whitespace normalization** for contiguous base representation

### Molecular Transformations
- **Complementarity mapping**: Watson-Crick pairing via bijective substitution
- **Transcriptional conversion**: thymine → uracil transposition
- **Reversal operator**: sequence inversion for anti-sense analysis
- **Translational engine**: codon → amino acid transduction with start/stop recognition
- **Compositional metrics**: GC content quantification

### Analytical Primitives
- **Nucleotide census**: per-base frequency enumeration
- **Reading frame awareness**: AUG-anchored translation with termination signaling

## Instantiation & Invocation

```python
from Genython import gen

# Initialize genomic object
genome = gen("sequence.fasta")

# Extract purified sequence
raw_sequence = genome.seq()

# Compute base distribution
base_counts = genome.getbases()

# Generate Watson-Crick complement
complement_strand = genome.complement()

# Transcribe to mRNA
mrna = genome.transcribe(complement_strand)

# Translate to polypeptide (start-to-stop)
protein = genome.translate(mrna)

# Calculate GC percentage
gc_ratio = genome.contentCG()
```

## Methodological Inventory

| Method         | Parameter(s)    | Return  | Operation                             |
|----------------|-----------------|---------|---------------------------------------|
| `seq()`        | —               | `str`   | Retrieve sanitized nucleotide string  |
| `getbases()`   | —               | `dict`  | Tally A, T, G, C frequencies          |
| `complement()` | —               | `str`   | Generate complementary strand         |
| `transcribe()` | `sequence: str` | `str`   | Convert DNA → RNA                     |
| `reverse()`    | —               | `str`   | Invert sequence directionality        |
| `translate()`  | `sequence: str` | `str`   | Decode mRNA → protein (AUG-initiated) |
| `contentCG()`  | —               | `float` | Compute GC percentage                 |

## Translational Mechanics

The `translate()` method implements biologically faithful peptide synthesis:

1. **Start codon detection**: Scans for initial `AUG` (methionine)
2. **Triplet segmentation**: Partitions from anchor point in 3-nucleotide increments
3. **Termination awareness**: Halts upon encountering `UAA`, `UAG`, or `UGA`
4. **Ambiguity handling**: Substitutes `X` for unrecognized or incomplete codons

## Compositional Analysis

**GC content** serves as phylogenetic fingerprint and structural predictor. The
metric correlates with:
- Thermal stability (triple vs. double hydrogen bonding)
- Gene density demarcation
- Taxonomic clustering
- Codon usage bias in thermophilic organisms

## Extensibility Vectors

Prospective augmentations:
- **Multi-frame ORF extraction** (±1, ±2, ±3 reading frames)
- **Pattern matching** via IUPAC-compliant regex
- **Sliding-window GC profiling** for heterogeneity cartography
- **Repeat element detection** (tandem, palindromic)
- **Format interoperability** (GenBank, GFF3 serialization)

## Technical Constraints

- **Input format**: FASTA with single-line header
- **Character set**: `{A, T, G, C, U}` (case-sensitive)
- **Genetic code**: Standard translation table (vertebrate mitochondrial variants unsupported)

## Authorship & Provenance

Conceived as instructional substrate for computational biology curricula.
Contributions welcome via fork-and-merge workflow.

