# Skema & Pohon Pembentukan Akun Kanonik (`canonical_account_tree`)

Dokumen ini memetakan **Resep Pembentukan (*Canonical Construction Schema*)** untuk seluruh **52 Akun Kanonik (`Canonical Schema`)** dari **[Neraca (`461 akun`)](balance_statement_accounts.md)**, **[Laba Rugi (`189 akun`)](income_statement_accounts.md)**, dan **[Arus Kas (`292 akun`)](cash_flow_statement_accounts.md)** berdasarkan kombinasi faktual `(Entry Point × Sector/Subsector × Variant)` di Bursa Efek Indonesia.

### Struktur Tabel Setiap Akun Kanonik
Setiap **Akun Kanonik** disajikan dalam blok tabel terstruktur:
1. **Baris Judul (`colspan=3`)**: Kode dan nama akun kanonik beserta jumlah total akun mentah lintas sektor.
2. **Baris Penjelasan (3 Kolom)**: **Penjelasan & Fungsi Kanonik** | **Aturan Agregasi** | **Makna Ekonomi & Saran Analisis**.
3. **Baris Profil Emiten (3 Kolom)**: **Entry Points** | **Sectors** | **Subsectors**.
4. **Baris Varian & Akun Pembentuk (2 Bagian: `1 Kolom + Colspan 2`)**: **Variant** di sisi kiri (`34%`) dan **Daftar Lengkap Akun Mentah Pembentuk (`+` / `−`)** di sisi kanan (`66%`).

---

## 1. Pemetaan Kanonik Neraca (`balance_statement` — 21 Akun Kanonik dari 488 Akun Mentah)

### 1.1 Aset Kanonik (`[CAN.BS.A]`)

<table width="100%">
  <colgroup>
    <col width="34%" />
    <col width="34%" />
    <col width="32%" />
  </colgroup>
  <thead>
    <tr>
      <th align="left" width="34%">Penjelasan / Entry Points / Variant</th>
      <th align="left" width="34%">Aturan Agregasi / Sectors / Accounts</th>
      <th align="left" width="32%">Makna Ekonomi &amp; Saran Analisis / Subsectors</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="3"><code>[CAN.BS.A]</code> <b><code>total_assets</code></b> &nbsp;<span><i>(Total 1 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Total Seluruh Aset Konsolidasi</b>: Jangkar utama ukuran neraca perusahaan di seluruh 8 <i>entry point</i>.</td>
      <td width="34%" valign="top"><b>Direct Anchor</b>: Ambil langsung dari <code>[A] Assets</code>. Jika kosong pada neraca terklasifikasi, <code>CurrentAssets + NonCurrentAssets</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan skala ekonomi dan total sumber daya yang dikendalikan perusahaan untuk menghasilkan pendapatan.<br/><b>Saran Analisis:</b> Gunakan sebagai pembagi utama untuk menghitung <b>ROA</b> (<code>net_income_parent / total_assets</code>) dan efisiensi perputaran aset (<b>Asset Turnover</b>).</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code>, <code>property</code>, <code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b> <code>all_variants</code><br/>• <code>current_and_non_current</code><br/>• <code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[A]</code> <code>Assets</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code>, <code>financing</code>, <code>insurance</code>, <code>securities</code>, <code>collective_investment_contract</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>B</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>I</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>B1</code>, <code>C1</code>, <code>E6</code>, <code>G1</code>, <code>G2</code>, <code>G3</code>, <code>G4</code>, <code>G5</code>, <code>H1</code>, <code>I2</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[A]</code> <code>Assets</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.A.C]</code> <b><code>total_current_assets</code></b> &nbsp;<span><i>(Total 1 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Total Aset Lancar (&lt; 12 Bulan)</b>: Total aset jangka pendek pada neraca terklasifikasi (<i>Classified Balance Sheet</i>).</td>
      <td width="34%" valign="top"><b>Direct / Sum</b>: Ambil dari <code>[A.C] CurrentAssets</code>. Pada neraca likuiditas (Bank, Multifinance, Asuransi, Sekuritas), diproksikan dari <code>cash_and_central_bank + marketable_securities_and_investments</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan total amunisi modal kerja jangka pendek yang siap berputar menjadi uang tunai dalam satu siklus operasi (&lt; 12 bulan).<br/><b>Saran Analisis:</b> Bandingkan terhadap <code>total_current_liabilities</code> untuk menghitung <b>Current Ratio</b> dan <b>Net Working Capital</b> pada sektor riil.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code>, <code>property</code>, <code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[A.C]</code> <code>CurrentAssets</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.A.N]</code> <b><code>total_non_current_assets</code></b> &nbsp;<span><i>(Total 1 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Total Aset Tidak Lancar (&gt; 12 Bulan)</b>: Total aset jangka panjang pada neraca terklasifikasi.</td>
      <td width="34%" valign="top"><b>Direct / Residual</b>: Ambil dari <code>[A.N] NonCurrentAssets</code>, atau <code>Assets − CurrentAssets</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan seberapa padat modal (<i>capital-intensive</i>) struktur bisnis perusahaan yang tertanam pada fasilitas fisik dan investasi jangka panjang.<br/><b>Saran Analisis:</b> Jika porsinya sangat dominan (&gt; 70% dari Total Aset), perusahaan memiliki beban tetap (penyusutan/pemeliharaan) yang tinggi sehingga sensitif terhadap penurunan utilisasi kapasitas.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code>, <code>property</code>, <code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[A.N]</code> <code>NonCurrentAssets</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.A.01]</code> <b><code>cash_and_central_bank</code></b> &nbsp;<span><i>(Total 13 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Kas, Setara Kas, Giro BI, &amp; Penempatan Antarbank</b>: Total likuiditas tunai lapis pertama (uang kas, bank, deposito &le; 3 bulan, Giro pada Bank Indonesia, dan penempatan pasar uang antarbank).</td>
      <td width="34%" valign="top"><b>Sum (Net of CKPN)</b>: Jumlahkan seluruh kas, deposito jangka sangat pendek, Giro BI, Giro pada Bank Lain, dan Penempatan pada BI/Bank Lain dikurangi CKPN terkait (<code>AllowanceForImpairmentLosses...</code>).</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan <b>daya tahan likuiditas instan (<i>survival buffer</i>)</b> perusahaan untuk membayar kewajiban mendesak tanpa harus menjual aset atau meminjam uang baru.<br/><b>Saran Analisis:</b> Kurangkan dari Total Utang Berbunga untuk menghitung <b>Net Debt</b>, serta bandingkan terhadap utang jangka pendek untuk menghitung <b>Cash Ratio</b>.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code>, <code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[A.C.01]</code> <code>CashAndCashEquivalents</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.02]</code> <code>CurrentDeposits</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.01]</code> <code>NonCurrentDeposits</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[A.C.01]</code> <code>CashAndCashEquivalents</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.01]</code> <code>Deposits</code> <i>[G5, K1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>C1</code>, <code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code>, <code>J3</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[A.C.01]</code> <code>CashAndCashEquivalents</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.02]</code> <code>CurrentDeposits</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.01]</code> <code>NonCurrentDeposits</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[A.C.01]</code> <code>CashAndCashEquivalents</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (9):</b><br/><code>+</code> <code>[A.L.20]</code> <code>Cash</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.21]</code> <code>Current<wbr>Accounts<wbr>With<wbr>Bank<wbr>Indonesia</code> <i>[G1, G5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.22]</code> <code>Current<wbr>Accounts<wbr>With<wbr>Other<wbr>Banks<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.23]</code> <code>Current<wbr>Accounts<wbr>With<wbr>Other<wbr>Banks<wbr>Related<wbr>Parties</code> <i>[G1]</i> &nbsp;·&nbsp; <code>−</code> <code>[A.L.24]</code> <code>Allowance<wbr>For<wbr>Impairment<wbr>Losses<wbr>For<wbr>Current<wbr>Accounts<wbr>With<wbr>Other<wbr>Banks</code> <i>[G1, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.25]</code> <code>Placements<wbr>With<wbr>Bank<wbr>Indonesia<wbr>And<wbr>Other<wbr>Banks<wbr>Third<wbr>Parties</code> <i>[G1, G5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.26]</code> <code>Placements<wbr>With<wbr>Bank<wbr>Indonesia<wbr>And<wbr>Other<wbr>Banks<wbr>Related<wbr>Parties</code> <i>[G1]</i> &nbsp;·&nbsp; <code>−</code> <code>[A.L.27]</code> <code>Allowance<wbr>For<wbr>Impairment<wbr>Losses<wbr>For<wbr>Placements<wbr>With<wbr>Other<wbr>Banks</code> <i>[G1, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.28]</code> <code>Interbank<wbr>Mudharabah<wbr>Investments</code> <i>[G1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (6):</b><br/><code>+</code> <code>[A.C.01]</code> <code>CashAndCashEquivalents</code> <i>[C1, G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.21]</code> <code>Current<wbr>Accounts<wbr>With<wbr>Bank<wbr>Indonesia</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.22]</code> <code>Current<wbr>Accounts<wbr>With<wbr>Other<wbr>Banks<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.23]</code> <code>Current<wbr>Accounts<wbr>With<wbr>Other<wbr>Banks<wbr>Related<wbr>Parties</code> <i>[E6, G2, I2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.25]</code> <code>Placements<wbr>With<wbr>Bank<wbr>Indonesia<wbr>And<wbr>Other<wbr>Banks<wbr>Third<wbr>Parties</code> <i>[C1, G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.26]</code> <code>Placements<wbr>With<wbr>Bank<wbr>Indonesia<wbr>And<wbr>Other<wbr>Banks<wbr>Related<wbr>Parties</code> <i>[G2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code>, <code>securities</code>, <code>collective_investment_contract</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>B</code>, <code>G</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>B1</code>, <code>G3</code>, <code>G4</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[A.C.01]</code> <code>CashAndCashEquivalents</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.A.02]</code> <b><code>restricted_cash_and_clearing_deposits</code></b> &nbsp;<span><i>(Total 4 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Dana yang Dibatasi Penggunaannya &amp; Jaminan Kliring</b>: Rekening bank yang dikunci sebagai jaminan utang/proyek (<i>escrow</i>) atau dana jaminan kliring di KPEI.</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan dana dibatasi penggunaannya (lancar, tidak lancar, likuiditas) + simpanan jaminan kliring KPEI.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan uang tunai milik perusahaan yang <b>sedang dikunci/dijaminkan</b> kepada kreditur, regulator, atau lembaga kliring sehingga tidak bebas dipakai operasional.<br/><b>Saran Analisis:</b> <b>Jangan pernah dimasukkan ke dalam Kas Bebas saat menghitung Net Debt!</b> Kenaikan pos ini menunjukkan makin banyak kas perusahaan yang tertahan sebagai agunan.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code>, <code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[A.C.03]</code> <code>CurrentRestrictedFunds</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.02]</code> <code>NonCurrentRestrictedFunds</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[A.L.02]</code> <code>RestrictedFunds</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[A.C.03]</code> <code>CurrentRestrictedFunds</code> <i>[61, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.02]</code> <code>NonCurrentRestrictedFunds</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code>, <code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G2</code>, <code>G3</code>, <code>G5</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[A.L.02]</code> <code>RestrictedFunds</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.29]</code> <code>Deposits<wbr>To<wbr>Clearing<wbr>And<wbr>Settlement<wbr>Guarantee<wbr>Institution</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.A.03]</code> <b><code>short_term_and_marketable_investments</code></b> &nbsp;<span><i>(Total 44 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Investasi Jangka Pendek, Surat Berharga (Efek), SBN, Reverse Repo, &amp; Portofolio Asuransi/KIK</b>: Cadangan likuiditas sekunder berupa efek FVTPL/FVOCI/Amortized Cost, Obligasi Pemerintah (SBN), tagihan <i>Reverse Repo</i>, derivatif, dan portofolio investasi asuransi/DIRE.</td>
      <td width="34%" valign="top"><b>Sum (Net of CKPN)</b>: Jumlahkan seluruh instrumen investasi keuangan dan efek surat berharga dikurangi CKPN efek (<code>AllowanceForImpairmentLossesForMarketableSecurities</code>).</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan cadangan likuiditas lapis kedua (<i>secondary liquidity</i>) sekaligus portofolio investasi penghasil imbal hasil (kupon/dividen/<i>capital gain</i>) pada bank, asuransi, dan korporasi.<br/><b>Saran Analisis:</b> Tambahkan ke <code>cash_and_central_bank</code> untuk menghitung <b>Total Liquid Assets</b> dan mengevaluasi kemampuan asuransi/bank memenuhi klaim atau penarikan dana.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (15):</b><br/><code>+</code> <code>[A.C.04]</code> <code>ShortTermInvestments</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.05]</code> <code>Current<wbr>Financial<wbr>Assets<wbr>At<wbr>Fair<wbr>Value<wbr>Through<wbr>Profit<wbr>Or<wbr>Loss</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.06]</code> <code>Current<wbr>Financial<wbr>Assets<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.07]</code> <code>Current<wbr>Financial<wbr>Assets<wbr>Amortized<wbr>Cost<wbr>Investments</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.08]</code> <code>Current<wbr>Financial<wbr>Assets<wbr>Held<wbr>To<wbr>Maturity<wbr>Investments</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.09]</code> <code>Current<wbr>Financial<wbr>Assets<wbr>Available<wbr>For<wbr>Sale</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.10]</code> <code>Current<wbr>Derivative<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.11]</code> <code>OtherCurrentFinancialAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.12]</code> <code>Other<wbr>Non<wbr>Current<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.03]</code> <code>Non<wbr>Current<wbr>Financial<wbr>Assets<wbr>At<wbr>Fair<wbr>Value<wbr>Through<wbr>Profit<wbr>Or<wbr>Loss</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.04]</code> <code>Non<wbr>Current<wbr>Financial<wbr>Assets<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.05]</code> <code>Non<wbr>Current<wbr>Financial<wbr>Assets<wbr>Amortized<wbr>Cost</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.06]</code> <code>Non<wbr>Current<wbr>Financial<wbr>Assets<wbr>Held<wbr>To<wbr>Maturity</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.07]</code> <code>Non<wbr>Current<wbr>Financial<wbr>Assets<wbr>Available<wbr>For<wbr>Sale</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.08]</code> <code>Non<wbr>Current<wbr>Derivative<wbr>Financial<wbr>Assets</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (8):</b><br/><code>+</code> <code>[A.C.04]</code> <code>ShortTermInvestments</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.03]</code> <code>Financial<wbr>Assets<wbr>At<wbr>Fair<wbr>Value<wbr>Through<wbr>Profit<wbr>Or<wbr>Loss</code> <i>[G3, G5, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.04]</code> <code>Financial<wbr>Assets<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.05]</code> <code>FinancialAssetsAmortizedCost</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.06]</code> <code>Financial<wbr>Assets<wbr>Held<wbr>To<wbr>Maturity</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.07]</code> <code>Financial<wbr>Assets<wbr>Available<wbr>For<wbr>Sale</code> <i>[G5, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.08]</code> <code>DerivativeFinancialAssets</code> <i>[E5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.09]</code> <code>OtherFinancialAssets</code> <i>[G5, J2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (15):</b><br/><code>+</code> <code>[A.C.04]</code> <code>ShortTermInvestments</code> <i>[E5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.05]</code> <code>Current<wbr>Financial<wbr>Assets<wbr>At<wbr>Fair<wbr>Value<wbr>Through<wbr>Profit<wbr>Or<wbr>Loss</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.06]</code> <code>Current<wbr>Financial<wbr>Assets<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.07]</code> <code>Current<wbr>Financial<wbr>Assets<wbr>Amortized<wbr>Cost<wbr>Investments</code> <i>[E5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.08]</code> <code>Current<wbr>Financial<wbr>Assets<wbr>Held<wbr>To<wbr>Maturity<wbr>Investments</code> <i>[E5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.09]</code> <code>Current<wbr>Financial<wbr>Assets<wbr>Available<wbr>For<wbr>Sale</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.10]</code> <code>Current<wbr>Derivative<wbr>Financial<wbr>Assets</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.11]</code> <code>OtherCurrentFinancialAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.12]</code> <code>Other<wbr>Non<wbr>Current<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.03]</code> <code>Non<wbr>Current<wbr>Financial<wbr>Assets<wbr>At<wbr>Fair<wbr>Value<wbr>Through<wbr>Profit<wbr>Or<wbr>Loss</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.04]</code> <code>Non<wbr>Current<wbr>Financial<wbr>Assets<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income</code> <i>[H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.05]</code> <code>Non<wbr>Current<wbr>Financial<wbr>Assets<wbr>Amortized<wbr>Cost</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.06]</code> <code>Non<wbr>Current<wbr>Financial<wbr>Assets<wbr>Held<wbr>To<wbr>Maturity</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.07]</code> <code>Non<wbr>Current<wbr>Financial<wbr>Assets<wbr>Available<wbr>For<wbr>Sale</code> <i>[H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.08]</code> <code>Non<wbr>Current<wbr>Derivative<wbr>Financial<wbr>Assets</code> <i>[H1, J2, K1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[A.L.07]</code> <code>Financial<wbr>Assets<wbr>Available<wbr>For<wbr>Sale</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.09]</code> <code>OtherFinancialAssets</code> <i>[H1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (14):</b><br/><code>+</code> <code>[A.C.04]</code> <code>ShortTermInvestments</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.05]</code> <code>Current<wbr>Financial<wbr>Assets<wbr>At<wbr>Fair<wbr>Value<wbr>Through<wbr>Profit<wbr>Or<wbr>Loss</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.06]</code> <code>Current<wbr>Financial<wbr>Assets<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income</code> <i>[J1, K1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.07]</code> <code>Current<wbr>Financial<wbr>Assets<wbr>Amortized<wbr>Cost<wbr>Investments</code> <i>[J2, J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.08]</code> <code>Current<wbr>Financial<wbr>Assets<wbr>Held<wbr>To<wbr>Maturity<wbr>Investments</code> <i>[J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.09]</code> <code>Current<wbr>Financial<wbr>Assets<wbr>Available<wbr>For<wbr>Sale</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.10]</code> <code>Current<wbr>Derivative<wbr>Financial<wbr>Assets</code> <i>[J1, J2, J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.03]</code> <code>Non<wbr>Current<wbr>Financial<wbr>Assets<wbr>At<wbr>Fair<wbr>Value<wbr>Through<wbr>Profit<wbr>Or<wbr>Loss</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.04]</code> <code>Non<wbr>Current<wbr>Financial<wbr>Assets<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income</code> <i>[J3, J4, K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.06]</code> <code>Non<wbr>Current<wbr>Financial<wbr>Assets<wbr>Held<wbr>To<wbr>Maturity</code> <i>[J2, J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.07]</code> <code>Non<wbr>Current<wbr>Financial<wbr>Assets<wbr>Available<wbr>For<wbr>Sale</code> <i>[J2, J3, K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.08]</code> <code>Non<wbr>Current<wbr>Derivative<wbr>Financial<wbr>Assets</code> <i>[A1, J1, J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.48]</code> <code>CurrentOtherFinancialAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.59]</code> <code>Non<wbr>Current<wbr>Other<wbr>Financial<wbr>Assets</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[A.L.09]</code> <code>OtherFinancialAssets</code> <i>[J2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (9):</b><br/><code>+</code> <code>[A.L.09]</code> <code>OtherFinancialAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.31]</code> <code>Marketable<wbr>Securities<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.32]</code> <code>Marketable<wbr>Securities<wbr>Related<wbr>Parties</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>−</code> <code>[A.L.33]</code> <code>Allowance<wbr>For<wbr>Impairment<wbr>Losses<wbr>For<wbr>Marketable<wbr>Securities</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.34]</code> <code>GovernmentBonds</code> <i>[G1, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.35]</code> <code>Securities<wbr>Purchased<wbr>Under<wbr>Agreement<wbr>To<wbr>Resale</code> <i>[G1, G5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.37]</code> <code>Derivative<wbr>Receivables<wbr>Third<wbr>Parties</code> <i>[G1, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.38]</code> <code>Derivative<wbr>Receivables<wbr>Related<wbr>Parties</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.47]</code> <code>Investments<wbr>Of<wbr>Policyholder<wbr>In<wbr>Unit<wbr>Linked<wbr>Contracts</code> <i>[G5]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (8):</b><br/><code>+</code> <code>[A.L.03]</code> <code>Financial<wbr>Assets<wbr>At<wbr>Fair<wbr>Value<wbr>Through<wbr>Profit<wbr>Or<wbr>Loss</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.04]</code> <code>Financial<wbr>Assets<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.05]</code> <code>FinancialAssetsAmortizedCost</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.06]</code> <code>Financial<wbr>Assets<wbr>Held<wbr>To<wbr>Maturity</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.07]</code> <code>Financial<wbr>Assets<wbr>Available<wbr>For<wbr>Sale</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.09]</code> <code>OtherFinancialAssets</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.35]</code> <code>Securities<wbr>Purchased<wbr>Under<wbr>Agreement<wbr>To<wbr>Resale</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.36]</code> <code>DerivativeReceivables</code> <i>[E6, G2, I2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (9):</b><br/><code>+</code> <code>[A.L.39]</code> <code>InvestmentsInTimeDeposits</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.40]</code> <code>InvestmentsInShares</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.42]</code> <code>Investments<wbr>On<wbr>Securities<wbr>And<wbr>Mutual<wbr>Funds<wbr>At<wbr>Fair<wbr>Value<wbr>Through<wbr>Profit<wbr>Or<wbr>Loss</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.43]</code> <code>Investments<wbr>On<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Securities</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.44]</code> <code>Investments<wbr>On<wbr>Available<wbr>For<wbr>Sale<wbr>Securities</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.45]</code> <code>Investments<wbr>On<wbr>Amortized<wbr>Cost<wbr>Securities</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.46]</code> <code>Investments<wbr>On<wbr>Held<wbr>To<wbr>Maturity<wbr>Securities</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.47]</code> <code>Investments<wbr>Of<wbr>Policyholder<wbr>In<wbr>Unit<wbr>Linked<wbr>Contracts</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.48]</code> <code>OtherInvestments</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[A.L.30]</code> <code>MarketableSecurities</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.35]</code> <code>Securities<wbr>Purchased<wbr>Under<wbr>Agreement<wbr>To<wbr>Resale</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.41]</code> <code>Investments<wbr>In<wbr>Shares<wbr>Of<wbr>Indonesia<wbr>Stock<wbr>Exchange</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>collective_investment_contract</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>B</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>B1</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[A.L.49]</code> <code>Securities<wbr>Portfolio<wbr>In<wbr>Equity<wbr>Instruments</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.A.04]</code> <b><code>trade_and_project_receivables</code></b> &nbsp;<span><i>(Total 17 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Piutang Usaha, Piutang Pelanggan, Piutang Retensi, &amp; Tagihan Proyek Sektor Riil</b>: Tagihan kepada pelanggan atas penjualan barang/jasa, piutang belum ditagih (<i>unbilled</i>), piutang retensi konstruksi, wesel tagih, piutang bunga/dividen, dan piutang subsidi pemerintah.</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan seluruh piutang usaha &amp; pelanggan (pihak ketiga &amp; berelasi), piutang retensi, piutang belum ditagih (<i>unbilled</i>), wesel tagih, piutang subsidi, dan piutang lain-lain pihak ketiga.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan <b>daya tawar perusahaan terhadap pelanggan</b> dan seberapa banyak omzet penjualan yang masih berupa tagihan di atas kertas (belum menjadi uang tunai).<br/><b>Saran Analisis:</b> Hitung <b>Days Sales Outstanding (DSO)</b> (<code>(trade_and_project_receivables / gross_revenue_real_sector) × 365</code>). Lonjakan DSO menandakan penagihan macet atau penjualan dipaksakan lewat kredit longgar.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (14):</b><br/><code>+</code> <code>[A.C.13]</code> <code>TradeReceivablesThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.14]</code> <code>Trade<wbr>Receivables<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.15]</code> <code>Unbilled<wbr>Receivables<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.16]</code> <code>Unbilled<wbr>Receivables<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.17]</code> <code>Retention<wbr>Receivables<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.18]</code> <code>Retention<wbr>Receivables<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.26]</code> <code>Current<wbr>Customer<wbr>Receivables<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.27]</code> <code>Current<wbr>Customer<wbr>Receivables<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.10]</code> <code>Non<wbr>Current<wbr>Customer<wbr>Receivables<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.11]</code> <code>Non<wbr>Current<wbr>Customer<wbr>Receivables<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.28]</code> <code>NotesReceivable</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.19]</code> <code>Dividends<wbr>And<wbr>Interest<wbr>Receivables</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.24]</code> <code>OtherReceivablesThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.30]</code> <code>Other<wbr>Non<wbr>Current<wbr>Receivables<wbr>Third<wbr>Parties</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (10):</b><br/><code>+</code> <code>[A.C.13]</code> <code>TradeReceivablesThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.14]</code> <code>Trade<wbr>Receivables<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.15]</code> <code>Unbilled<wbr>Receivables<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.16]</code> <code>Unbilled<wbr>Receivables<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.17]</code> <code>Retention<wbr>Receivables<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.18]</code> <code>Retention<wbr>Receivables<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.10]</code> <code>Customer<wbr>Receivables<wbr>Third<wbr>Parties</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.11]</code> <code>Customer<wbr>Receivables<wbr>Related<wbr>Parties</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.19]</code> <code>Dividends<wbr>And<wbr>Interest<wbr>Receivables</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.24]</code> <code>OtherReceivablesThirdParties</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>C1</code>, <code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code>, <code>J3</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (8):</b><br/><code>+</code> <code>[A.C.13]</code> <code>TradeReceivablesThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.14]</code> <code>Trade<wbr>Receivables<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.15]</code> <code>Unbilled<wbr>Receivables<wbr>Third<wbr>Parties</code> <i>[H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.16]</code> <code>Unbilled<wbr>Receivables<wbr>Related<wbr>Parties</code> <i>[H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.17]</code> <code>Retention<wbr>Receivables<wbr>Third<wbr>Parties</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.18]</code> <code>Retention<wbr>Receivables<wbr>Related<wbr>Parties</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.24]</code> <code>OtherReceivablesThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.30]</code> <code>Other<wbr>Non<wbr>Current<wbr>Receivables<wbr>Third<wbr>Parties</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[A.C.13]</code> <code>TradeReceivablesThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.15]</code> <code>Unbilled<wbr>Receivables<wbr>Third<wbr>Parties</code> <i>[H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.17]</code> <code>Retention<wbr>Receivables<wbr>Third<wbr>Parties</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.24]</code> <code>OtherReceivablesThirdParties</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>C</code>, <code>D</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>C1</code>, <code>D1</code>, <code>D2</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (5):</b><br/><code>+</code> <code>[A.C.13]</code> <code>TradeReceivablesThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.14]</code> <code>Trade<wbr>Receivables<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.49]</code> <code>ReceivablesOnSubsidy</code> <i>[J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.24]</code> <code>OtherReceivablesThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.30]</code> <code>Other<wbr>Non<wbr>Current<wbr>Receivables<wbr>Third<wbr>Parties</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[A.C.13]</code> <code>TradeReceivablesThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.14]</code> <code>Trade<wbr>Receivables<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.24]</code> <code>OtherReceivablesThirdParties</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[A.C.24]</code> <code>OtherReceivablesThirdParties</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.A.05]</code> <b><code>related_party_non_trade_receivables</code></b> &nbsp;<span><i>(Total 4 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Piutang Non-Usaha Pihak Berelasi &amp; Piutang Pemegang Saham</b>: Pinjaman uang tunai di luar piutang dagang yang diberikan perusahaan kepada perusahaan afiliasi/induk/pemegang saham.</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan piutang pihak berelasi non-usaha (lancar &amp; tidak lancar) serta piutang pemegang saham.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan seberapa banyak uang perusahaan publik yang <b>dipinjamkan ke luar operasi untuk membiayai perusahaan afiliasi/grup pemilik</b>.<br/><b>Saran Analisis:</b> <b>Indikator utama risiko Tata Kelola (GCG)!</b> Rasio <code>related_party_non_trade_receivables / total_assets</code> &gt; 5% merupakan <i>red flag</i> kebocoran kas ke grup pemegang saham pengendali.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[A.C.25]</code> <code>Other<wbr>Receivables<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.31]</code> <code>Other<wbr>Non<wbr>Current<wbr>Receivables<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.09]</code> <code>Receivables<wbr>From<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.13]</code> <code>ReceivablesFromStockholders</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[A.C.25]</code> <code>Other<wbr>Receivables<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.09]</code> <code>Receivables<wbr>From<wbr>Related<wbr>Parties</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[A.C.25]</code> <code>Other<wbr>Receivables<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.31]</code> <code>Other<wbr>Non<wbr>Current<wbr>Receivables<wbr>Related<wbr>Parties</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.09]</code> <code>Receivables<wbr>From<wbr>Related<wbr>Parties</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[A.N.09]</code> <code>Receivables<wbr>From<wbr>Related<wbr>Parties</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>D</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>D1</code>, <code>D2</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[A.C.25]</code> <code>Other<wbr>Receivables<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.31]</code> <code>Other<wbr>Non<wbr>Current<wbr>Receivables<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.09]</code> <code>Receivables<wbr>From<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.13]</code> <code>ReceivablesFromStockholders</code> <i>[J2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[A.C.25]</code> <code>Other<wbr>Receivables<wbr>Related<wbr>Parties</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G5</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[A.C.25]</code> <code>Other<wbr>Receivables<wbr>Related<wbr>Parties</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>E6</code>, <code>G2</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[A.N.09]</code> <code>Receivables<wbr>From<wbr>Related<wbr>Parties</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.A.06]</code> <b><code>loans_and_sharia_financing_net</code></b> &nbsp;<span><i>(Total 46 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Kredit Perbankan, Pembiayaan Syariah, &amp; Piutang Multifinance Bersih (<i>Net Loans &amp; Financing</i>)</b>: Total baki debet kredit konvensional, piutang murabahah/musyarakah/mudharabah/qardh/istishna/ijarah, pembiayaan konsumen, sewa pembiayaan (<i>finance lease</i>), anjak piutang (<i>factoring</i>), akseptasi, dan wesel ekspor setelah dikurangi CKPN &amp; pendapatan pembiayaan tangguhan.</td>
      <td width="34%" valign="top"><b>Sum (Gross − Contra/CKPN)</b>: Jumlahkan seluruh baki debet kredit &amp; pembiayaan bruto dikurangi seluruh akun <code>AllowanceForImpairmentLosses...</code> dan <code>...DeferredFinancingIncome</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan <b>mesin penghasil bunga/bagi hasil utama (<i>core earning assets</i>)</b> bagi Bank dan Multifinance setelah memperhitungkan risiko kredit macet (CKPN).<br/><b>Saran Analisis:</b> Gunakan untuk menghitung <b>LDR / FDR</b> (<code>loans_and_sharia_financing_net / Total DPK</code>) dan memantau pertumbuhan penyaluran kredit bersih.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>B</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>I</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>B1</code>, <code>C1</code>, <code>C2</code>, <code>C3</code>, <code>E6</code>, <code>E7</code>, <code>G5</code>, <code>I2</code>, <code>J4</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[A.C.29]</code> <code>Current<wbr>Finance<wbr>Lease<wbr>Receivables</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.12]</code> <code>Non<wbr>Current<wbr>Finance<wbr>Lease<wbr>Receivables</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[A.L.12]</code> <code>FinanceLeaseReceivables</code> <i>[G5]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[A.N.12]</code> <code>Non<wbr>Current<wbr>Finance<wbr>Lease<wbr>Receivables</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>J</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[A.C.29]</code> <code>Current<wbr>Finance<wbr>Lease<wbr>Receivables</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.12]</code> <code>Non<wbr>Current<wbr>Finance<wbr>Lease<wbr>Receivables</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (39):</b><br/><code>+</code> <code>[A.L.50]</code> <code>LoansThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.51]</code> <code>LoansRelatedParties</code> &nbsp;·&nbsp; <code>−</code> <code>[A.L.52]</code> <code>Allowance<wbr>For<wbr>Impairment<wbr>Losses<wbr>For<wbr>Loans</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.53]</code> <code>Consumer<wbr>Financing<wbr>Receivables<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.54]</code> <code>Consumer<wbr>Financing<wbr>Receivables<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>−</code> <code>[A.L.55]</code> <code>Allowance<wbr>For<wbr>Impairment<wbr>Losses<wbr>For<wbr>Consumer<wbr>Financing<wbr>Receivables</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.56]</code> <code>Murabahah<wbr>Receivables<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.57]</code> <code>Murabahah<wbr>Receivables<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>−</code> <code>[A.L.58]</code> <code>Allowance<wbr>For<wbr>Impairment<wbr>Losses<wbr>For<wbr>Murabahah<wbr>Receivables</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.59]</code> <code>Musyarakah<wbr>Financing<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.60]</code> <code>Musyarakah<wbr>Financing<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>−</code> <code>[A.L.61]</code> <code>Allowance<wbr>For<wbr>Impairment<wbr>Losses<wbr>For<wbr>Musyarakah<wbr>Financing</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.62]</code> <code>Mudharabah<wbr>Financing<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.63]</code> <code>Mudharabah<wbr>Financing<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>−</code> <code>[A.L.64]</code> <code>Allowance<wbr>For<wbr>Impairment<wbr>Losses<wbr>For<wbr>Mudharabah<wbr>Financing</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.65]</code> <code>QardhFundsThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.66]</code> <code>QardhFundsRelatedParties</code> &nbsp;·&nbsp; <code>−</code> <code>[A.L.67]</code> <code>Allowance<wbr>For<wbr>Impairment<wbr>Losses<wbr>For<wbr>Qardh<wbr>Funds</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.68]</code> <code>Istishna<wbr>Receivables<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.69]</code> <code>Istishna<wbr>Receivables<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>−</code> <code>[A.L.70]</code> <code>Allowance<wbr>For<wbr>Impairment<wbr>Losses<wbr>For<wbr>Istishna<wbr>Receivables</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.71]</code> <code>Ijarah<wbr>Receivables<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.72]</code> <code>Ijarah<wbr>Receivables<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>−</code> <code>[A.L.73]</code> <code>Allowance<wbr>For<wbr>Impairment<wbr>Losses<wbr>For<wbr>Ijarah<wbr>Receivables</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.75]</code> <code>LeaseInvestmentsThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.76]</code> <code>Lease<wbr>Investments<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.77]</code> <code>Lease<wbr>Investments<wbr>Guaranteed<wbr>Residual<wbr>Value</code> &nbsp;·&nbsp; <code>−</code> <code>[A.L.78]</code> <code>Lease<wbr>Investments<wbr>Deferred<wbr>Financing<wbr>Income</code> &nbsp;·&nbsp; <code>−</code> <code>[A.L.79]</code> <code>Lease<wbr>Investments<wbr>Guarantee<wbr>Deposits</code> &nbsp;·&nbsp; <code>−</code> <code>[A.L.80]</code> <code>Allowance<wbr>For<wbr>Impairment<wbr>Losses<wbr>For<wbr>Lease<wbr>Investments</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.81]</code> <code>Factoring<wbr>Receivables<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.82]</code> <code>Factoring<wbr>Receivables<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>−</code> <code>[A.L.84]</code> <code>Allowance<wbr>For<wbr>Impairment<wbr>Losses<wbr>For<wbr>Factoring<wbr>Receivables</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.86]</code> <code>Acceptance<wbr>Receivables<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.87]</code> <code>Acceptance<wbr>Receivables<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>−</code> <code>[A.L.88]</code> <code>Allowance<wbr>For<wbr>Impairment<wbr>Losses<wbr>For<wbr>Acceptance<wbr>Receivables</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.90]</code> <code>Bills<wbr>And<wbr>Other<wbr>Receivables<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.91]</code> <code>Bills<wbr>And<wbr>Other<wbr>Receivables<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>−</code> <code>[A.L.92]</code> <code>Allowance<wbr>For<wbr>Impairment<wbr>Losses<wbr>For<wbr>Bills<wbr>And<wbr>Other<wbr>Receivables</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (22):</b><br/><code>+</code> <code>[A.L.50]</code> <code>LoansThirdParties</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.51]</code> <code>LoansRelatedParties</code> <i>[G5]</i> &nbsp;·&nbsp; <code>−</code> <code>[A.L.52]</code> <code>Allowance<wbr>For<wbr>Impairment<wbr>Losses<wbr>For<wbr>Loans</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.53]</code> <code>Consumer<wbr>Financing<wbr>Receivables<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.54]</code> <code>Consumer<wbr>Financing<wbr>Receivables<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.56]</code> <code>Murabahah<wbr>Receivables<wbr>Third<wbr>Parties</code> <i>[E6, G2, I2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.57]</code> <code>Murabahah<wbr>Receivables<wbr>Related<wbr>Parties</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.59]</code> <code>Musyarakah<wbr>Financing<wbr>Third<wbr>Parties</code> <i>[E6, G2, I2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.60]</code> <code>Musyarakah<wbr>Financing<wbr>Related<wbr>Parties</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.71]</code> <code>Ijarah<wbr>Receivables<wbr>Third<wbr>Parties</code> <i>[C1, G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.72]</code> <code>Ijarah<wbr>Receivables<wbr>Related<wbr>Parties</code> <i>[C1, G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.74]</code> <code>Lease<wbr>Investment<wbr>In<wbr>Finance<wbr>Leases</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.75]</code> <code>LeaseInvestmentsThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.76]</code> <code>Lease<wbr>Investments<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.77]</code> <code>Lease<wbr>Investments<wbr>Guaranteed<wbr>Residual<wbr>Value</code> &nbsp;·&nbsp; <code>−</code> <code>[A.L.78]</code> <code>Lease<wbr>Investments<wbr>Deferred<wbr>Financing<wbr>Income</code> &nbsp;·&nbsp; <code>−</code> <code>[A.L.79]</code> <code>Lease<wbr>Investments<wbr>Guarantee<wbr>Deposits</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.81]</code> <code>Factoring<wbr>Receivables<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.82]</code> <code>Factoring<wbr>Receivables<wbr>Related<wbr>Parties</code> <i>[C1, G5]</i> &nbsp;·&nbsp; <code>−</code> <code>[A.L.83]</code> <code>Factoring<wbr>Receivables<wbr>On<wbr>Deferred<wbr>Factoring<wbr>Income</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.85]</code> <code>AcceptanceReceivables</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.89]</code> <code>BillsAndOtherReceivables</code> <i>[G5]</i></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.A.07]</code> <b><code>securities_and_insurance_receivables_net</code></b> &nbsp;<span><i>(Total 23 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Piutang Perusahaan Efek (Broker/Nasabah/Margin) &amp; Piutang Premi/Reasuransi Bersih</b>: Tagihan transaksi bursa sekuritas (KPEI, broker, nasabah, MI) serta tagihan premi, koasuransi, reasuransi, aset reasuransi/retrosesi, dan piutang lain-lain keuangan setelah dikurangi CKPN.</td>
      <td width="34%" valign="top"><b>Sum (Net of CKPN)</b>: Jumlahkan seluruh piutang sekuritas, piutang premi/reasuransi, aset reasuransi/retrosesi, dan piutang lain-lain keuangan dikurangi CKPN terkait.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan eksposur tagihan transaksi bursa/margin pada Perusahaan Efek serta tagihan premi dan klaim reasuransi pada Perusahaan Asuransi.<br/><b>Saran Analisis:</b> Jika porsi piutang premi/reasuransi membengkak terhadap ekuitas asuransi, waspadai risiko gagal tagih (<i>counterparty risk</i>) dari perusahaan reasuransi.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C3</code>, <code>E4</code>, <code>E7</code>, <code>G5</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b> <code>all_variants</code><br/>• <code>current_and_non_current</code><br/>• <code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[A.C.20]</code> <code>MarginReceivables</code> <i>[E4, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.21]</code> <code>Receivables<wbr>From<wbr>Clearing<wbr>And<wbr>Settlement<wbr>Guarantee<wbr>Institution</code> <i>[C3, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.22]</code> <code>Premium<wbr>And<wbr>Reinsurance<wbr>Receivables</code> <i>[C3, E7, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.23]</code> <code>ReinsuranceAssets</code> <i>[C3, E7, G5]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (9):</b><br/><code>+</code> <code>[A.C.21]</code> <code>Receivables<wbr>From<wbr>Clearing<wbr>And<wbr>Settlement<wbr>Guarantee<wbr>Institution</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.94]</code> <code>Receivables<wbr>From<wbr>Customers<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.95]</code> <code>Receivables<wbr>From<wbr>Customers<wbr>Related<wbr>Parties</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>−</code> <code>[A.L.96]</code> <code>Allowance<wbr>For<wbr>Impairment<wbr>Losses<wbr>For<wbr>Receivables<wbr>From<wbr>Customers</code> <i>[G1, G2, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.23]</code> <code>ReinsuranceAssets</code> <i>[G4, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.107]</code> <code>Insurance<wbr>Receivables<wbr>Third<wbr>Parties</code> <i>[G4, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.108]</code> <code>Insurance<wbr>Receivables<wbr>Related<wbr>Parties</code> <i>[G5]</i> &nbsp;·&nbsp; <code>−</code> <code>[A.L.109]</code> <code>Allowance<wbr>For<wbr>Impairment<wbr>Losses<wbr>For<wbr>Insurance<wbr>Receivables</code> <i>[G5]</i> &nbsp;·&nbsp; <code>−</code> <code>[A.L.111]</code> <code>Allowance<wbr>For<wbr>Impairment<wbr>Losses<wbr>For<wbr>Other<wbr>Receivables</code> <i>[G1, G5]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[A.C.23]</code> <code>ReinsuranceAssets</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.106]</code> <code>InsuranceReceivables</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.110]</code> <code>OtherReceivables</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (8):</b><br/><code>+</code> <code>[A.C.23]</code> <code>ReinsuranceAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.100]</code> <code>PremiumReceivables</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.101]</code> <code>CoinsuranceReceivables</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.102]</code> <code>ReinsuranceReceivables</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.103]</code> <code>RetrocessionReceivables</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.104]</code> <code>RetrocessionAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.105]</code> <code>InvestmentIncomeReceivables</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.110]</code> <code>OtherReceivables</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (9):</b><br/><code>+</code> <code>[A.C.20]</code> <code>MarginReceivables</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.21]</code> <code>Receivables<wbr>From<wbr>Clearing<wbr>And<wbr>Settlement<wbr>Guarantee<wbr>Institution</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.93]</code> <code>ReceivablesFromBrokers</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.94]</code> <code>Receivables<wbr>From<wbr>Customers<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.95]</code> <code>Receivables<wbr>From<wbr>Customers<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.97]</code> <code>Receivables<wbr>From<wbr>Investment<wbr>Manager</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.98]</code> <code>Receivables<wbr>From<wbr>Underwriting<wbr>And<wbr>Advisory<wbr>Services</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.99]</code> <code>AccruedIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.110]</code> <code>OtherReceivables</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>collective_investment_contract</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>B</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>B1</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[A.L.110]</code> <code>OtherReceivables</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.A.08]</code> <b><code>inventories_and_biological_assets</code></b> &nbsp;<span><i>(Total 17 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Persediaan, Aset Biologis, &amp; Persediaan Real Estat Siap Jual</b>: Stok bahan baku, barang setengah jadi, barang jadi, ternak/tanaman biologis, serta tanah/bangunan properti yang sedang dibangun untuk dijual.</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan <code>CurrentInventories</code>, <code>NonCurrentInventories</code>, <code>OtherInventories</code>, aset biologis/ternak, dan aset real estat lancar/likuiditas.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan kecepatan perputaran barang dagangan/produksi, siklus tanam agrikultur, atau cadangan lahan/properti siap jual (<i>landbank &amp; inventory</i>).<br/><b>Saran Analisis:</b> Hitung <b>Days Inventory Outstanding (DIO)</b> (<code>(inventories_and_biological_assets / cost_of_revenue_real_sector) × 365</code>). DIO yang membengkak menandakan stok menumpuk/tidak laku (<i>dead stock</i>).</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (15):</b><br/><code>+</code> <code>[A.C.32]</code> <code>CurrentInventories</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.33]</code> <code>CurrentLivestockInventories</code> <i>[D2, E3, E5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.34]</code> <code>CurrentBiologicalAssets</code> <i>[A1, B1, D2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.35]</code> <code>CurrentRealEstateAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.14]</code> <code>NonCurrentInventories</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.15]</code> <code>LivestockProduction</code> <i>[D2, E3]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.16]</code> <code>Non-CurrentBiologicalAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.17]</code> <code>PlantationAssetsMature</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.18]</code> <code>PlantationAssetsImmature</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.19]</code> <code>PlasmaPlantations</code> <i>[B1, C3, D2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.20]</code> <code>Industrial<wbr>Timber<wbr>Plantations<wbr>Mature</code> <i>[B1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.21]</code> <code>Industrial<wbr>Timber<wbr>Plantations<wbr>Immature</code> <i>[B1, D2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.22]</code> <code>Deferred<wbr>Charges<wbr>On<wbr>Cost<wbr>On<wbr>Forest</code> <i>[B1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.23]</code> <code>NonCurrentRealEstateAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.24]</code> <code>UndevelopedLand</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[A.L.13]</code> <code>Inventories</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>C1</code>, <code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (5):</b><br/><code>+</code> <code>[A.C.32]</code> <code>CurrentInventories</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.35]</code> <code>CurrentRealEstateAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.14]</code> <code>NonCurrentInventories</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.23]</code> <code>NonCurrentRealEstateAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.24]</code> <code>UndevelopedLand</code> <i>[E5, H1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[A.L.13]</code> <code>Inventories</code> <i>[H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.112]</code> <code>RealEstateAssets</code> <i>[H1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>C</code>, <code>D</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>C1</code>, <code>D1</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (5):</b><br/><code>+</code> <code>[A.C.32]</code> <code>CurrentInventories</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.35]</code> <code>CurrentRealEstateAssets</code> <i>[J2, K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.14]</code> <code>NonCurrentInventories</code> <i>[J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.23]</code> <code>NonCurrentRealEstateAssets</code> <i>[A1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.13]</code> <code>Inventories</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[A.L.13]</code> <code>Inventories</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.A.09]</code> <b><code>prepaid_expenses_advances_and_taxes</code></b> &nbsp;<span><i>(Total 28 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Biaya Dibayar di Muka, Uang Muka (<i>Advances</i>), &amp; Pajak Dibayar di Muka / Restitusi</b>: Pembayaran di muka operasional, DP pembelian aset/proyek, PPN masukan, dan klaim restitusi pajak.</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan seluruh biaya dibayar di muka, uang muka lancar/tidak lancar, pajak dibayar di muka, dan klaim restitusi pajak.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan kas yang sudah dikeluarkan di muka untuk biaya operasional, uang muka pemasok/investasi, atau kelebihan bayar pajak yang menunggu restitusi.<br/><b>Saran Analisis:</b> Bukan aset likuid penutup utang; jika uang muka investasi/proyek menggantung terlalu lama tanpa menjadi aset tetap, waspadai proyek mangkrak atau transaksi fiktif.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (17):</b><br/><code>+</code> <code>[A.N.25]</code> <code>Guarantees</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.36]</code> <code>CurrentPrepaidExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.37]</code> <code>CurrentAdvancesOnInvestments</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.38]</code> <code>Current<wbr>Advances<wbr>On<wbr>Purchase<wbr>Of<wbr>Property<wbr>Plant<wbr>And<wbr>Equipment</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.39]</code> <code>OtherCurrentAdvances</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.40]</code> <code>OtherNonCurrentAdvances</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.41]</code> <code>CurrentGuarantees</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.42]</code> <code>CurrentPrepaidTaxes</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.43]</code> <code>CurrentClaimsForTaxRefund</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.44]</code> <code>CurrentTaxAmnestyAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.26]</code> <code>NonCurrentPrepaidExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.27]</code> <code>Non<wbr>Current<wbr>Advances<wbr>On<wbr>Investments</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.28]</code> <code>Non<wbr>Current<wbr>Advances<wbr>On<wbr>Purchase<wbr>Of<wbr>Property<wbr>Plant<wbr>And<wbr>Equipment</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.29]</code> <code>NonCurrentGuarantees</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.30]</code> <code>NonCurrentPrepaidTaxes</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.31]</code> <code>NonCurrentClaimsForTaxRefund</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.32]</code> <code>NonCurrentTaxAmnestyAssets</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (6):</b><br/><code>+</code> <code>[A.N.25]</code> <code>Guarantees</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.14]</code> <code>PrepaidExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.15]</code> <code>Advances<wbr>On<wbr>Purchase<wbr>Of<wbr>Property<wbr>Plant<wbr>And<wbr>Equipment</code> <i>[E1, E5, E6]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.16]</code> <code>OtherAdvances</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.17]</code> <code>PrepaidTaxes</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.18]</code> <code>ClaimsForTaxRefund</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>C1</code>, <code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code>, <code>J3</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (16):</b><br/><code>+</code> <code>[A.N.25]</code> <code>Guarantees</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.36]</code> <code>CurrentPrepaidExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.37]</code> <code>CurrentAdvancesOnInvestments</code> <i>[61, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.39]</code> <code>OtherCurrentAdvances</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.40]</code> <code>OtherNonCurrentAdvances</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.41]</code> <code>CurrentGuarantees</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.42]</code> <code>CurrentPrepaidTaxes</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.44]</code> <code>CurrentTaxAmnestyAssets</code> <i>[E3, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.26]</code> <code>NonCurrentPrepaidExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.27]</code> <code>Non<wbr>Current<wbr>Advances<wbr>On<wbr>Investments</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.29]</code> <code>NonCurrentGuarantees</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.30]</code> <code>NonCurrentPrepaidTaxes</code> <i>[E5, G5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.31]</code> <code>NonCurrentClaimsForTaxRefund</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.32]</code> <code>NonCurrentTaxAmnestyAssets</code> <i>[E3, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.51]</code> <code>Current<wbr>Advances<wbr>On<wbr>Purchase<wbr>Of<wbr>Property<wbr>And<wbr>Equipment</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.61]</code> <code>Non<wbr>Current<wbr>Advances<wbr>On<wbr>Purchase<wbr>Of<wbr>Property<wbr>And<wbr>Equipment</code> <i>[E5, H1, J2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[A.L.14]</code> <code>PrepaidExpenses</code> <i>[H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.17]</code> <code>PrepaidTaxes</code> <i>[H1, J2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>C</code>, <code>D</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>C1</code>, <code>D2</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (13):</b><br/><code>+</code> <code>[A.N.25]</code> <code>Guarantees</code> <i>[J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.36]</code> <code>CurrentPrepaidExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.41]</code> <code>CurrentGuarantees</code> <i>[A1, J1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.42]</code> <code>CurrentPrepaidTaxes</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.43]</code> <code>CurrentClaimsForTaxRefund</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.44]</code> <code>CurrentTaxAmnestyAssets</code> <i>[J2, J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.26]</code> <code>NonCurrentPrepaidExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.29]</code> <code>NonCurrentGuarantees</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.30]</code> <code>NonCurrentPrepaidTaxes</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.31]</code> <code>NonCurrentClaimsForTaxRefund</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.32]</code> <code>NonCurrentTaxAmnestyAssets</code> <i>[J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.50]</code> <code>CurrentAdvances</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.60]</code> <code>NonCurrentAdvances</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[A.L.14]</code> <code>PrepaidExpenses</code> <i>[J2, K1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.17]</code> <code>PrepaidTaxes</code> <i>[J2, K1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.113]</code> <code>Advances</code> <i>[J2, K1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (6):</b><br/><code>+</code> <code>[A.N.25]</code> <code>Guarantees</code> <i>[G1, G4, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.14]</code> <code>PrepaidExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.17]</code> <code>PrepaidTaxes</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.18]</code> <code>ClaimsForTaxRefund</code> <i>[G1, G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.113]</code> <code>Advances</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.114]</code> <code>TaxAmnestyAssets</code> <i>[G1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (5):</b><br/><code>+</code> <code>[A.N.25]</code> <code>Guarantees</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.14]</code> <code>PrepaidExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.17]</code> <code>PrepaidTaxes</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.18]</code> <code>ClaimsForTaxRefund</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.114]</code> <code>TaxAmnestyAssets</code> <i>[G2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[A.N.25]</code> <code>Guarantees</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.14]</code> <code>PrepaidExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.17]</code> <code>PrepaidTaxes</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (5):</b><br/><code>+</code> <code>[A.L.14]</code> <code>PrepaidExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.17]</code> <code>PrepaidTaxes</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.18]</code> <code>ClaimsForTaxRefund</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.113]</code> <code>Advances</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.114]</code> <code>TaxAmnestyAssets</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>collective_investment_contract</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>B</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>B1</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[A.L.17]</code> <code>PrepaidTaxes</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.A.10]</code> <b><code>ppe_and_productive_real_assets</code></b> &nbsp;<span><i>(Total 10 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Aset Tetap, Aset Hak Guna (ROU), Properti Investasi, Tambang, Migas, &amp; Hak Konsesi</b>: Seluruh aset fisik produktif jangka panjang (pabrik, mesin, gedung, kebun, hutan, properti tambang/migas, jalan tol, dan aset sewa operasi/ijarah).</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan <code>PropertyPlantAndEquipment</code>, <code>PropertyAndEquipment</code>, <code>RightofuseAssets</code>, <code>InvestmentProperties</code>, aset tambang/migas/konsesi tol, dan <code>IjarahAssets</code> / <code>OperatingLeaseAssets</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan <b>tulang punggung kapasitas produksi fisik</b> perusahaan (pabrik, mesin, jaringan tol, kebun, tambang, armada) untuk mencetak pendapatan jangka panjang.<br/><b>Saran Analisis:</b> Hitung <b>Fixed Asset Turnover</b> (<code>gross_revenue_real_sector / ppe_and_productive_real_assets</code>) untuk mengukur produktivitas mesin/fasilitas fisik dalam menghasilkan omzet.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (8):</b><br/><code>+</code> <code>[A.N.33]</code> <code>PropertyPlantAndEquipment</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.43]</code> <code>IjarahAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.47]</code> <code>MiningProperties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.48]</code> <code>Exploration<wbr>And<wbr>Evaluation<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.49]</code> <code>OilAndGasAssets</code> <i>[A1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.50]</code> <code>Non<wbr>Current<wbr>Deferred<wbr>Stripping<wbr>Costs</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.51]</code> <code>Deferred<wbr>Charges<wbr>On<wbr>Exploration<wbr>And<wbr>Development<wbr>Expenditures</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.53]</code> <code>TollRoadConcessionRights</code> <i>[C3]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[A.N.33]</code> <code>PropertyPlantAndEquipment</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.43]</code> <code>IjarahAssets</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>C1</code>, <code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code>, <code>J3</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[A.N.33]</code> <code>PropertyPlantAndEquipment</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.62]</code> <code>PropertyAndEquipment</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[A.N.62]</code> <code>PropertyAndEquipment</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>C</code>, <code>D</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>C1</code>, <code>D1</code>, <code>D2</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[A.N.33]</code> <code>PropertyPlantAndEquipment</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.53]</code> <code>TollRoadConcessionRights</code> <i>[J1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.62]</code> <code>PropertyAndEquipment</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[A.N.33]</code> <code>PropertyPlantAndEquipment</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.62]</code> <code>PropertyAndEquipment</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[A.N.33]</code> <code>PropertyPlantAndEquipment</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.43]</code> <code>IjarahAssets</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.62]</code> <code>PropertyAndEquipment</code> <i>[G1, G4, G5]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[A.N.33]</code> <code>PropertyPlantAndEquipment</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.43]</code> <code>IjarahAssets</code> <i>[C1, G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.62]</code> <code>PropertyAndEquipment</code> <i>[C1, G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.115]</code> <code>OperatingLeaseAssets</code> <i>[G2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code>, <code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G3</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[A.N.33]</code> <code>PropertyPlantAndEquipment</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.62]</code> <code>PropertyAndEquipment</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.A.11]</code> <b><code>intangible_assets_and_goodwill</code></b> &nbsp;<span><i>(Total 8 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Goodwill &amp; Aset Takberwujud Lainnya</b>: Selisih lebih harga akuisisi anak usaha (<i>Goodwill</i>) ditambah lisensi software, paten, hak merek, dan beban tangguhan.</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan <code>Goodwill</code>, <code>IntangibleAssetsOtherThanGoodwill</code>, <code>OtherIntangibleAssets</code>, dan beban tangguhan.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan nilai premi akuisisi masa lalu (<i>Goodwill</i>) dan hak eksklusif non-fisik (lisensi, merek, paten) yang tidak memiliki wujud fisik.<br/><b>Saran Analisis:</b> <b>Kurangkan dari Ekuitas untuk menghitung Tangible Book Value (TBV)!</b> Emiten dengan Goodwill besar berisiko mengalami rugi penurunan nilai (<i>impairment</i>) mendadak jika anak usaha yang dibeli berkinerja buruk.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (7):</b><br/><code>+</code> <code>[A.N.39]</code> <code>Goodwill</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.40]</code> <code>Intangible<wbr>Assets<wbr>Other<wbr>Than<wbr>Goodwill</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.42]</code> <code>OtherDeferredCharges</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.45]</code> <code>Current<wbr>Deferred<wbr>Mobilisation<wbr>Costs</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.52]</code> <code>Deferred<wbr>Charges<wbr>On<wbr>Environmental<wbr>And<wbr>Reclamation<wbr>Expenditures</code> <i>[A1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.54]</code> <code>DeferredChargesOnLandrights</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.55]</code> <code>Non<wbr>Current<wbr>Deferred<wbr>Mobilisation<wbr>Costs</code> <i>[E6]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[A.N.39]</code> <code>Goodwill</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.40]</code> <code>Intangible<wbr>Assets<wbr>Other<wbr>Than<wbr>Goodwill</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.42]</code> <code>OtherDeferredCharges</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>C</code>, <code>E</code>, <code>H</code>, <code>J</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>C1</code>, <code>E3</code>, <code>E5</code>, <code>H1</code>, <code>J2</code>, <code>J3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[A.N.39]</code> <code>Goodwill</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.40]</code> <code>Intangible<wbr>Assets<wbr>Other<wbr>Than<wbr>Goodwill</code> <i>[E5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.42]</code> <code>OtherDeferredCharges</code> <i>[61, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.54]</code> <code>DeferredChargesOnLandrights</code> <i>[H1, J2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>D</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>D2</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[A.N.39]</code> <code>Goodwill</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.40]</code> <code>Intangible<wbr>Assets<wbr>Other<wbr>Than<wbr>Goodwill</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.42]</code> <code>OtherDeferredCharges</code> <i>[A1, J2, K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.63]</code> <code>DeferredCharges</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[A.N.42]</code> <code>OtherDeferredCharges</code> <i>[A1, J2, K2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code>, <code>financing</code>, <code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G3</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[A.N.39]</code> <code>Goodwill</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.40]</code> <code>Intangible<wbr>Assets<wbr>Other<wbr>Than<wbr>Goodwill</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[A.N.40]</code> <code>Intangible<wbr>Assets<wbr>Other<wbr>Than<wbr>Goodwill</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.A.12]</code> <b><code>long_term_investments_and_other_assets</code></b> &nbsp;<span><i>(Total 16 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Investasi pada Entitas Asosiasi/JV, Aset Pajak Tangguhan, AYDA, &amp; Aset Lain-lain</b>: Penyertaan saham metode ekuitas (asosiasi/JV), aset pajak tangguhan, agunan kredit diambil alih (AYDA), aset dimiliki untuk dijual, dan aset rupa-rupa.</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan investasi asosiasi/JV/anak usaha, <code>DeferredTaxAssets</code>, <code>ForeclosedAssets</code>, aset imbalan pascakerja, dan aset lain-lain.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan penyertaan bisnis non-pengendali (perusahaan asosiasi/JV), tabungan pengurang pajak masa depan (pajak tangguhan), serta aset sitaan kredit macet (AYDA).<br/><b>Saran Analisis:</b> Pada Bank/Multifinance, lonjakan <code>ForeclosedAssets (AYDA)</code> menggambarkan banyaknya agunan debitur macet yang terpaksa diambil alih namun belum berhasil dicairkan menjadi kas.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (14):</b><br/><code>+</code> <code>[A.N.34]</code> <code>RightOfUseAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.35]</code> <code>InvestmentProperties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.36]</code> <code>InvestmentsInAssociates</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.37]</code> <code>InvestmentsInJointVentures</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.38]</code> <code>Investments<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.41]</code> <code>DeferredTaxAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.44]</code> <code>ForeclosedAssets</code> <i>[A1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.45]</code> <code>Non<wbr>Current<wbr>Assets<wbr>Or<wbr>Disposal<wbr>Groups<wbr>Classified<wbr>As<wbr>Held<wbr>For<wbr>Sale</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.46]</code> <code>Other<wbr>Current<wbr>Non<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.47]</code> <code>Other<wbr>Non<wbr>Current<wbr>Non<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.46]</code> <code>InvestmentsInSubsidiaries</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.56]</code> <code>Aircraft<wbr>Maintenance<wbr>Reserve<wbr>Funds</code> <i>[K1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.57]</code> <code>PostEmploymentBenefitAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.58]</code> <code>Non<wbr>Current<wbr>Assets<wbr>Or<wbr>Disposal<wbr>Groups<wbr>Classified<wbr>As<wbr>Held<wbr>For<wbr>Distribution<wbr>To<wbr>Owners</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (9):</b><br/><code>+</code> <code>[A.N.34]</code> <code>RightOfUseAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.35]</code> <code>InvestmentProperties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.36]</code> <code>InvestmentsInAssociates</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.37]</code> <code>InvestmentsInJointVentures</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.38]</code> <code>Investments<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.41]</code> <code>DeferredTaxAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.44]</code> <code>ForeclosedAssets</code> <i>[A1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.45]</code> <code>Non<wbr>Current<wbr>Assets<wbr>Or<wbr>Disposal<wbr>Groups<wbr>Classified<wbr>As<wbr>Held<wbr>For<wbr>Sale</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.19]</code> <code>OtherNonFinancialAssets</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>C1</code>, <code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code>, <code>J3</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (11):</b><br/><code>+</code> <code>[A.N.34]</code> <code>RightOfUseAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.35]</code> <code>InvestmentProperties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.36]</code> <code>InvestmentsInAssociates</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.37]</code> <code>InvestmentsInJointVentures</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.38]</code> <code>Investments<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.41]</code> <code>DeferredTaxAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.45]</code> <code>Non<wbr>Current<wbr>Assets<wbr>Or<wbr>Disposal<wbr>Groups<wbr>Classified<wbr>As<wbr>Held<wbr>For<wbr>Sale</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.C.46]</code> <code>Other<wbr>Current<wbr>Non<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.47]</code> <code>Other<wbr>Non<wbr>Current<wbr>Non<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.46]</code> <code>InvestmentsInSubsidiaries</code> <i>[H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.57]</code> <code>PostEmploymentBenefitAssets</code> <i>[H1, J2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (6):</b><br/><code>+</code> <code>[A.N.35]</code> <code>InvestmentProperties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.36]</code> <code>InvestmentsInAssociates</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.38]</code> <code>Investments<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.41]</code> <code>DeferredTaxAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.46]</code> <code>InvestmentsInSubsidiaries</code> <i>[H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.19]</code> <code>OtherNonFinancialAssets</code> <i>[H1, J2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>C</code>, <code>D</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>C1</code>, <code>D1</code>, <code>D2</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (12):</b><br/><code>+</code> <code>[A.N.34]</code> <code>RightOfUseAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.35]</code> <code>InvestmentProperties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.36]</code> <code>InvestmentsInAssociates</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.37]</code> <code>InvestmentsInJointVentures</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.38]</code> <code>Investments<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.41]</code> <code>DeferredTaxAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.45]</code> <code>Non<wbr>Current<wbr>Assets<wbr>Or<wbr>Disposal<wbr>Groups<wbr>Classified<wbr>As<wbr>Held<wbr>For<wbr>Sale</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.46]</code> <code>Other<wbr>Current<wbr>Non<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.C.47]</code> <code>Other<wbr>Non<wbr>Current<wbr>Non<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.46]</code> <code>InvestmentsInSubsidiaries</code> <i>[J2, K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.56]</code> <code>Aircraft<wbr>Maintenance<wbr>Reserve<wbr>Funds</code> <i>[K1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.57]</code> <code>PostEmploymentBenefitAssets</code> <i>[J3, K2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[A.N.34]</code> <code>RightOfUseAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.41]</code> <code>DeferredTaxAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.58]</code> <code>Non<wbr>Current<wbr>Assets<wbr>Or<wbr>Disposal<wbr>Groups<wbr>Classified<wbr>As<wbr>Held<wbr>For<wbr>Distribution<wbr>To<wbr>Owners</code> <i>[J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.19]</code> <code>OtherNonFinancialAssets</code> <i>[K1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (11):</b><br/><code>+</code> <code>[A.N.34]</code> <code>RightOfUseAssets</code> <i>[G1, G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.35]</code> <code>InvestmentProperties</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.36]</code> <code>InvestmentsInAssociates</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.37]</code> <code>InvestmentsInJointVentures</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.38]</code> <code>Investments<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.41]</code> <code>DeferredTaxAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.44]</code> <code>ForeclosedAssets</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.45]</code> <code>Non<wbr>Current<wbr>Assets<wbr>Or<wbr>Disposal<wbr>Groups<wbr>Classified<wbr>As<wbr>Held<wbr>For<wbr>Sale</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.46]</code> <code>InvestmentsInSubsidiaries</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.57]</code> <code>PostEmploymentBenefitAssets</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.116]</code> <code>OtherAssets</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (7):</b><br/><code>+</code> <code>[A.N.34]</code> <code>RightOfUseAssets</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.35]</code> <code>InvestmentProperties</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.36]</code> <code>InvestmentsInAssociates</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.38]</code> <code>Investments<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.N.41]</code> <code>DeferredTaxAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.44]</code> <code>ForeclosedAssets</code> <i>[C1, G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[A.L.116]</code> <code>OtherAssets</code> <i>[C1, G2, G5]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (6):</b><br/><code>+</code> <code>[A.N.34]</code> <code>RightOfUseAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.35]</code> <code>InvestmentProperties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.41]</code> <code>DeferredTaxAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.45]</code> <code>Non<wbr>Current<wbr>Assets<wbr>Or<wbr>Disposal<wbr>Groups<wbr>Classified<wbr>As<wbr>Held<wbr>For<wbr>Sale</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.57]</code> <code>PostEmploymentBenefitAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.116]</code> <code>OtherAssets</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[A.N.35]</code> <code>InvestmentProperties</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.36]</code> <code>InvestmentsInAssociates</code> &nbsp;·&nbsp; <code>+</code> <code>[A.N.41]</code> <code>DeferredTaxAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[A.L.116]</code> <code>OtherAssets</code></td>
    </tr>
  </tbody>
</table>

### 1.2 Liabilitas & Dana Syirkah Temporer Kanonik (`[CAN.BS.L]` & `[CAN.BS.S]`)

<table width="100%">
  <colgroup>
    <col width="34%" />
    <col width="34%" />
    <col width="32%" />
  </colgroup>
  <thead>
    <tr>
      <th align="left" width="34%">Penjelasan / Entry Points / Variant</th>
      <th align="left" width="34%">Aturan Agregasi / Sectors / Accounts</th>
      <th align="left" width="32%">Makna Ekonomi &amp; Saran Analisis / Subsectors</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="3"><code>[CAN.BS.L]</code> <b><code>total_liabilities</code></b> &nbsp;<span><i>(Total 1 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Total Liabilitas</b>: Total seluruh kewajiban perusahaan (utang jangka pendek + utang jangka panjang).</td>
      <td width="34%" valign="top"><b>Direct Anchor</b>: Ambil dari <code>[L] Liabilities</code>, atau <code>CurrentLiabilities + NonCurrentLiabilities</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan total beban kewajiban finansial dan operasional perusahaan kepada pihak luar yang harus dilunasi di masa depan.<br/><b>Saran Analisis:</b> Bandingkan dengan <code>total_assets</code> (<b>Debt-to-Assets</b>) dan <code>total_equity_or_net_assets</code> untuk mengukur tingkat <i>leverage</i> struktur modal.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code>, <code>property</code>, <code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b> <code>all_variants</code><br/>• <code>current_and_non_current</code><br/>• <code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[L]</code> <code>Liabilities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code>, <code>financing</code>, <code>insurance</code>, <code>securities</code>, <code>collective_investment_contract</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>B</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>I</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>B1</code>, <code>C1</code>, <code>E6</code>, <code>G1</code>, <code>G2</code>, <code>G3</code>, <code>G4</code>, <code>G5</code>, <code>H1</code>, <code>I2</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[L]</code> <code>Liabilities</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.L.C]</code> <b><code>total_current_liabilities</code></b> &nbsp;<span><i>(Total 1 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Total Liabilitas Jangka Pendek (&lt; 12 Bulan)</b>: Seluruh kewajiban yang jatuh tempo dalam 1 tahun pada neraca terklasifikasi.</td>
      <td width="34%" valign="top"><b>Direct</b>: Ambil dari <code>[L.C] CurrentLiabilities</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan seluruh tagihan dan utang yang <b>wajib dilunasi dalam 12 bulan ke depan</b>, yang menentukan tekanan likuiditas jangka pendek perusahaan.<br/><b>Saran Analisis:</b> Penyebut utama <b>Current Ratio</b> dan <b>Quick Ratio</b>; jika lebih besar dari Aset Lancar (<i>Working Capital</i> negatif), perusahaan menghadapi risiko gagal bayar jangka pendek.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code>, <code>property</code>, <code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[L.C]</code> <code>CurrentLiabilities</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.L.N]</code> <b><code>total_non_current_liabilities</code></b> &nbsp;<span><i>(Total 1 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Total Liabilitas Jangka Panjang (&gt; 12 Bulan)</b>: Seluruh kewajiban yang jatuh tempo lebih dari 1 tahun pada neraca terklasifikasi.</td>
      <td width="34%" valign="top"><b>Direct</b>: Ambil dari <code>[L.N] NonCurrentLiabilities</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan komitmen pendanaan jangka panjang (&gt; 1 tahun) yang memberi ruang napas waktu sebelum jatuh tempo.<br/><b>Saran Analisis:</b> Pastikan arus kas operasional tahunan (EBITDA / OCF) cukup kuat untuk menutup beban bunga dan jadwal cicilan pokok jangka panjang.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code>, <code>property</code>, <code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[L.N]</code> <code>NonCurrentLiabilities</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.L.01]</code> <b><code>customer_and_interbank_deposits</code></b> &nbsp;<span><i>(Total 16 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Simpanan Nasabah (Dana Pihak Ketiga / DPK Konvensional &amp; Wadiah) dan Simpanan Bank Lain</b>: Giro, Tabungan, Deposito Berjangka, Simpanan Wadiah/Wakalah, Liabilitas Segera, serta Simpanan dari Bank Lain.</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan seluruh akun Giro, Tabungan, Deposito nasabah, simpanan syariah wadiah/wakalah, dan simpanan bank lain.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan <b>kekuatan pendanaan masyarakat (Dana Pihak Ketiga / DPK)</b> dan kepercayaan nasabah terhadap bank.<br/><b>Saran Analisis:</b> Hitung rasio dana murah <b>CASA</b> (Giro + Tabungan dibagi Total DPK); semakin tinggi CASA, semakin rendah biaya bunga (<i>Cost of Fund</i>) dan semakin tebal margin NIM bank.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (16):</b><br/><code>+</code> <code>[L.L.18]</code> <code>ObligationsDueImmediately</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.19]</code> <code>CurrentAccountsThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.20]</code> <code>Current<wbr>Accounts<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.21]</code> <code>SavingsThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.22]</code> <code>SavingsRelatedParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.23]</code> <code>TimeDepositsThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.24]</code> <code>TimeDepositsRelatedParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.25]</code> <code>Wadiah<wbr>Demand<wbr>Deposits<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.26]</code> <code>Wadiah<wbr>Demand<wbr>Deposits<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.27]</code> <code>WadiahSavingsThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.28]</code> <code>WadiahSavingsRelatedParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.29]</code> <code>ShariaDeposits</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.30]</code> <code>WakalahDepositsThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.31]</code> <code>OtherBanksDeposits</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.32]</code> <code>Other<wbr>Banks<wbr>Deposits<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.33]</code> <code>Other<wbr>Bankds<wbr>Deposits<wbr>Related<wbr>Parties</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[L.L.18]</code> <code>ObligationsDueImmediately</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.S]</code> <b><code>temporary_syirkah_and_tabarru_funds</code></b> &nbsp;<span><i>(Total 13 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Dana Syirkah Temporer (DST) &amp; Akumulasi Dana Tabarru'</b>: Simpanan dan investasi nasabah bank/asuransi syariah dengan akad bagi hasil (<i>Mudharabah / Musyarakah</i>) serta dana kebajikan klaim peserta (<i>Tabarru'</i>).</td>
      <td width="34%" valign="top"><b>Priority / Sum</b>: Ambil dari <code>[S] TemporarySyirkahFunds</code> + <code>AccumulatedTabarrusFunds</code>, atau jumlahkan komponen giro/tabungan/deposito mudharabah jika totalnya kosong.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan dana investasi bagi hasil nasabah (<i>Mudharabah/Musyarakah</i>) dan dana kumpulan klaim peserta (<i>Tabarru'</i>) pada perbankan/asuransi syariah.<br/><b>Saran Analisis:</b> <b>Wajib ditambahkan ke <code>customer_and_interbank_deposits</code></b> saat menghitung Total DPK dan rasio intermediasi <b>FDR</b> pada Bank Syariah.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (12):</b><br/><code>+</code> <code>[S]</code> <code>TemporarySyirkahFunds</code> &nbsp;·&nbsp; <code>+</code> <code>[S.01]</code> <code>MudharabahCurrentAccount</code> &nbsp;·&nbsp; <code>+</code> <code>[S.02]</code> <code>Mudharabah<wbr>Current<wbr>Account<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[S.03]</code> <code>Mudharabah<wbr>Current<wbr>Account<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[S.04]</code> <code>Mudharabah<wbr>Saving<wbr>Deposits<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[S.05]</code> <code>Mudharabah<wbr>Saving<wbr>Deposits<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[S.06]</code> <code>Mudharabah<wbr>Saving<wbr>Deposits<wbr>Ummat</code> &nbsp;·&nbsp; <code>+</code> <code>[S.07]</code> <code>MudharabahTimeDeposits</code> &nbsp;·&nbsp; <code>+</code> <code>[S.08]</code> <code>Mudharabah<wbr>Time<wbr>Deposits<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[S.09]</code> <code>Mudharabah<wbr>Time<wbr>Deposits<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[S.11]</code> <code>UndistributedProfitSharing</code> &nbsp;·&nbsp; <code>+</code> <code>[S.12]</code> <code>AccumulatedTabarrusFunds</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[S]</code> <code>TemporarySyirkahFunds</code> &nbsp;·&nbsp; <code>+</code> <code>[S.10]</code> <code>Mudharabah<wbr>Temporary<wbr>Syirkah<wbr>Funds</code> &nbsp;·&nbsp; <code>+</code> <code>[S.12]</code> <code>AccumulatedTabarrusFunds</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.L.02]</code> <b><code>short_term_and_working_capital_debt</code></b> &nbsp;<span><i>(Total 22 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Utang Bank Jangka Pendek &amp; Bagian Utang Jangka Panjang Jatuh Tempo &lt; 1 Tahun (<i>Short-Term Debt / CPLTD</i>)</b>: Pinjaman modal kerja jangka pendek ditambah porsi pokok pinjaman bank, obligasi, sukuk, MTN, wesel bayar, dan sewa yang jatuh tempo dalam 12 bulan ke depan.</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan seluruh fasilitas pinjaman jangka pendek (<code>ShortTermBankLoans</code>, dll.) dan seluruh akun <code>CurrentMaturitiesOf...</code> serta <code>CurrentLeaseLiabilities</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan <b>tekanan jatuh tempo utang berbunga dalam 1 tahun ke depan (<i>Refinancing &amp; Default Risk</i>)</b>.<br/><b>Saran Analisis:</b> Bandingkan langsung dengan <code>cash_and_central_bank + operating_cash_flow</code>. Jika kas dan OCF jauh lebih kecil dari akun ini, emiten sangat bergantung pada <i>roll-over</i> utang bank.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (18):</b><br/><code>+</code> <code>[L.C.01]</code> <code>ShortTermLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.02]</code> <code>ShortTermBankLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.03]</code> <code>CurrentMaturitiesOfBankLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.04]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Non-Bank<wbr>Financial<wbr>Institutions<wbr>Loan</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.05]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Secured<wbr>Loans</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.06]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Unsecured<wbr>Loans</code> <i>[A1, D2, F1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.07]</code> <code>CurrentMaturitiesOfStepLoans</code> <i>[E4]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.08]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Loans<wbr>From<wbr>Government<wbr>Of<wbr>The<wbr>Republic<wbr>Of<wbr>Indonesia</code> <i>[A1, B1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.09]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Other<wbr>Borrowings</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.10]</code> <code>TrustReceiptsPayables</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.12]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Bonds<wbr>Payable</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.13]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Subordinated<wbr>Bonds</code> <i>[B1, I1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.14]</code> <code>CurrentMaturitiesOfSukuk</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.15]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Medium<wbr>Term<wbr>Notes</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.16]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Notes<wbr>Payable</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.17]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Finance<wbr>Lease<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.18]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Consumer<wbr>Financing<wbr>Payables</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.19]</code> <code>Short<wbr>Term<wbr>Derivative<wbr>Financial<wbr>Liabilities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[L.C.01]</code> <code>ShortTermLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.02]</code> <code>ShortTermNonBankLoans</code> <i>[E5]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>C1</code>, <code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code>, <code>J3</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (13):</b><br/><code>+</code> <code>[L.C.01]</code> <code>ShortTermLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.02]</code> <code>ShortTermBankLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.03]</code> <code>CurrentMaturitiesOfBankLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.05]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Secured<wbr>Loans</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.06]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Unsecured<wbr>Loans</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.09]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Other<wbr>Borrowings</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.02]</code> <code>ShortTermNonBankLoans</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.61]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Subordinated<wbr>Loans</code> <i>[E5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.12]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Bonds<wbr>Payable</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.14]</code> <code>CurrentMaturitiesOfSukuk</code> <i>[E5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.15]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Medium<wbr>Term<wbr>Notes</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.16]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Notes<wbr>Payable</code> <i>[H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.17]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Finance<wbr>Lease<wbr>Liabilities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[L.C.01]</code> <code>ShortTermLoans</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>C</code>, <code>D</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>C1</code>, <code>D1</code>, <code>D2</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (17):</b><br/><code>+</code> <code>[L.C.01]</code> <code>ShortTermLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.02]</code> <code>ShortTermBankLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.03]</code> <code>CurrentMaturitiesOfBankLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.05]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Secured<wbr>Loans</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.06]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Unsecured<wbr>Loans</code> <i>[K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.07]</code> <code>CurrentMaturitiesOfStepLoans</code> <i>[J3, J4]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.09]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Other<wbr>Borrowings</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.02]</code> <code>ShortTermNonBankLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.62]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Land<wbr>Acquisition<wbr>Liabilities</code> <i>[J1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.12]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Bonds<wbr>Payable</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.13]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Subordinated<wbr>Bonds</code> <i>[J1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.14]</code> <code>CurrentMaturitiesOfSukuk</code> <i>[J2, J3, K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.15]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Medium<wbr>Term<wbr>Notes</code> <i>[J2, J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.16]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Notes<wbr>Payable</code> <i>[J4]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.17]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Finance<wbr>Lease<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.19]</code> <code>Short<wbr>Term<wbr>Derivative<wbr>Financial<wbr>Liabilities</code> <i>[J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.63]</code> <code>Current<wbr>Maturities<wbr>Notes<wbr>Payable</code> <i>[J3]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[L.L.02]</code> <code>ShortTermNonBankLoans</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>G2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[L.C.02]</code> <code>ShortTermBankLoans</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.L.03]</code> <b><code>long_term_loans_and_borrowings</code></b> &nbsp;<span><i>(Total 19 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Pinjaman Bank Jangka Panjang, Pinjaman Diterima (<i>Wholesale Borrowings</i>), &amp; Pinjaman Subordinasi</b>: Fasilitas kredit investasi jangka panjang (&gt; 1 tahun) serta pinjaman bilateral/sindikasi yang diterima oleh bank, multifinance, dan sekuritas.</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan seluruh akun <code>LongTerm...Loans</code>, <code>Borrowings...</code>, <code>SubordinatedLoans...</code>, dan utang pihak berelasi/pemegang saham jangka panjang.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan ketergantungan perusahaan pada kredit investasi perbankan dan pinjaman bilateral/sindikasi jangka panjang.<br/><b>Saran Analisis:</b> Komponen inti <b>Total Interest-Bearing Debt</b> untuk menghitung <b>Net Debt / EBITDA</b> dan <b>Debt-to-Equity Ratio (DER)</b>.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (8):</b><br/><code>+</code> <code>[L.C.11]</code> <code>FactoringPayables</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.01]</code> <code>LongTermBankLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.02]</code> <code>Long<wbr>Term<wbr>Non-Bank<wbr>Financial<wbr>Institutions<wbr>Loan</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.03]</code> <code>LongTermSecuredLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.04]</code> <code>LongTermUnsecuredLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.05]</code> <code>LongTermStepLoans</code> <i>[C2, E4]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.N.06]</code> <code>LongTermSubordinatedLoans</code> <i>[E4, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.N.07]</code> <code>LongTermOtherBorrowings</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[L.L.01]</code> <code>BankLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.03]</code> <code>OtherBorrowings</code> <i>[E1, E5, J2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>C1</code>, <code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (5):</b><br/><code>+</code> <code>[L.N.01]</code> <code>LongTermBankLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.02]</code> <code>Long<wbr>Term<wbr>Non-Bank<wbr>Financial<wbr>Institutions<wbr>Loan</code> <i>[G5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.N.03]</code> <code>LongTermSecuredLoans</code> <i>[61, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.N.04]</code> <code>LongTermUnsecuredLoans</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.N.07]</code> <code>LongTermOtherBorrowings</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[L.L.01]</code> <code>BankLoans</code> <i>[H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.03]</code> <code>OtherBorrowings</code> <i>[J2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>C</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>C1</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (7):</b><br/><code>+</code> <code>[L.N.01]</code> <code>LongTermBankLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.02]</code> <code>Long<wbr>Term<wbr>Non-Bank<wbr>Financial<wbr>Institutions<wbr>Loan</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.03]</code> <code>LongTermSecuredLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.04]</code> <code>LongTermUnsecuredLoans</code> <i>[J3, K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.N.05]</code> <code>LongTermStepLoans</code> <i>[A1, J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.N.07]</code> <code>LongTermOtherBorrowings</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.34]</code> <code>Long<wbr>Term<wbr>Land<wbr>Acquisition<wbr>Liabilities</code> <i>[J1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[L.L.01]</code> <code>BankLoans</code> <i>[J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.34]</code> <code>Non-Bank<wbr>Financial<wbr>Institutions<wbr>Loan</code> <i>[J2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (6):</b><br/><code>+</code> <code>[L.L.35]</code> <code>BorrowingsThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.36]</code> <code>BorrowingsRelatedParties</code> <i>[G1, G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.37]</code> <code>MidTermLoans</code> <i>[G1, G4]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.39]</code> <code>Subordinated<wbr>Loans<wbr>Third<wbr>Parties</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.40]</code> <code>Subordinated<wbr>Loans<wbr>Related<wbr>Parties</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.41]</code> <code>Borrowings<wbr>Payables<wbr>To<wbr>Clearing<wbr>And<wbr>Settlement<wbr>Guarantee<wbr>Institution</code> <i>[G2, G5]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (6):</b><br/><code>+</code> <code>[L.N.01]</code> <code>LongTermBankLoans</code> <i>[C1, G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.01]</code> <code>BankLoans</code> <i>[C1, G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.35]</code> <code>BorrowingsThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.36]</code> <code>BorrowingsRelatedParties</code> <i>[E6, G2, I2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.37]</code> <code>MidTermLoans</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.38]</code> <code>SubordinatedLoans</code> <i>[G2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[L.L.01]</code> <code>BankLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.38]</code> <code>SubordinatedLoans</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.L.04]</code> <b><code>bonds_sukuk_repo_and_lease_liabilities</code></b> &nbsp;<span><i>(Total 28 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Obligasi, Sukuk, MTN, Wesel Bayar, Liabilitas Repo, Akseptasi, Sewa Jangka Panjang, &amp; Derivatif</b>: Surat utang pasar modal jangka panjang, pendanaan <i>Repo</i>, kewajiban akseptasi L/C, liabilitas sewa pembiayaan (PSAK 73), dan liabilitas derivatif.</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan seluruh obligasi, sukuk, MTN, wesel bayar jangka panjang, <code>SecuritiesSoldWithRepurchaseAgreement</code>, liabilitas akseptasi, <code>NonCurrentLeaseLiabilities</code>, dan liabilitas derivatif.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan pendanaan jangka panjang dari pasar modal (Obligasi/Sukuk/MTN), pasar uang (Repo), dan kewajiban sewa jangka panjang (PSAK 73).<br/><b>Saran Analisis:</b> Jumlahkan <code>[CAN.BS.L.02] + [CAN.BS.L.03] + [CAN.BS.L.04]</code> untuk mendapatkan <b>Total Interest-Bearing Debt</b> yang komprehensif.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (9):</b><br/><code>+</code> <code>[L.N.08]</code> <code>ConvertibleBonds</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.09]</code> <code>LongTermBondsPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.10]</code> <code>LongTermSubordinatedBonds</code> <i>[E7]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.N.11]</code> <code>LongTermSukuk</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.12]</code> <code>LongTermMediumTermNotes</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.13]</code> <code>LongTermNotesPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.14]</code> <code>Long<wbr>Term<wbr>Finance<wbr>Lease<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.15]</code> <code>Long<wbr>Term<wbr>Consumer<wbr>Financing<wbr>Payables</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.16]</code> <code>Long<wbr>Term<wbr>Derivative<wbr>Financial<wbr>Liabilities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (5):</b><br/><code>+</code> <code>[L.N.08]</code> <code>ConvertibleBonds</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.04]</code> <code>BondsPayable</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.05]</code> <code>FinanceLeaseLiabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.06]</code> <code>ConsumerFinancingPayables</code> <i>[C2, E1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.07]</code> <code>Derivative<wbr>Financial<wbr>Liabilities</code> <i>[E5]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>C1</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code>, <code>J3</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (7):</b><br/><code>+</code> <code>[L.N.09]</code> <code>LongTermBondsPayable</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.N.10]</code> <code>LongTermSubordinatedBonds</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.N.11]</code> <code>LongTermSukuk</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.N.12]</code> <code>LongTermMediumTermNotes</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.N.13]</code> <code>LongTermNotesPayable</code> <i>[61, H1, K1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.N.14]</code> <code>Long<wbr>Term<wbr>Finance<wbr>Lease<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.16]</code> <code>Long<wbr>Term<wbr>Derivative<wbr>Financial<wbr>Liabilities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[L.L.05]</code> <code>FinanceLeaseLiabilities</code> <i>[J2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>D</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>D1</code>, <code>D2</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (7):</b><br/><code>+</code> <code>[L.N.08]</code> <code>ConvertibleBonds</code> <i>[J2, K1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.N.09]</code> <code>LongTermBondsPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.11]</code> <code>LongTermSukuk</code> <i>[J2, J3, K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.N.12]</code> <code>LongTermMediumTermNotes</code> <i>[J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.N.13]</code> <code>LongTermNotesPayable</code> <i>[J3, J4]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.N.14]</code> <code>Long<wbr>Term<wbr>Finance<wbr>Lease<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.16]</code> <code>Long<wbr>Term<wbr>Derivative<wbr>Financial<wbr>Liabilities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[L.L.04]</code> <code>BondsPayable</code> <i>[K1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.05]</code> <code>FinanceLeaseLiabilities</code> <i>[J2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (16):</b><br/><code>+</code> <code>[L.L.04]</code> <code>BondsPayable</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.05]</code> <code>FinanceLeaseLiabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.42]</code> <code>Securities<wbr>Sold<wbr>With<wbr>Repurchase<wbr>Agreement</code> <i>[G1, G5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.43]</code> <code>Bonds</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.44]</code> <code>Sukuk</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.45]</code> <code>MudharabahSukuk</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.46]</code> <code>IjarahSukuk</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.47]</code> <code>SubordinatedBonds</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.48]</code> <code>SubordinatedMudharabahSukuk</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.49]</code> <code>MediumTermNotes</code> <i>[G4]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.50]</code> <code>OthersSecuritiesIssued</code> <i>[G1, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.51]</code> <code>AcceptancePayables</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.52]</code> <code>Acceptance<wbr>Liabilities<wbr>Third<wbr>Parties</code> <i>[G1, G5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.53]</code> <code>Acceptance<wbr>Liabilities<wbr>Related<wbr>Parties</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.55]</code> <code>Derivative<wbr>Payables<wbr>Third<wbr>Parties</code> <i>[G1, G5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.56]</code> <code>Derivative<wbr>Payables<wbr>Related<wbr>Parties</code> <i>[G1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (8):</b><br/><code>+</code> <code>[L.L.04]</code> <code>BondsPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.05]</code> <code>FinanceLeaseLiabilities</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.42]</code> <code>Securities<wbr>Sold<wbr>With<wbr>Repurchase<wbr>Agreement</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.43]</code> <code>Bonds</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.45]</code> <code>MudharabahSukuk</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.50]</code> <code>OthersSecuritiesIssued</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.51]</code> <code>AcceptancePayables</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.54]</code> <code>DerivativePayables</code> <i>[E6, G2, I2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[L.L.04]</code> <code>BondsPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.05]</code> <code>FinanceLeaseLiabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.44]</code> <code>Sukuk</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[L.L.04]</code> <code>BondsPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.49]</code> <code>MediumTermNotes</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.L.05]</code> <b><code>trade_and_operational_payables</code></b> &nbsp;<span><i>(Total 32 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Utang Usaha, Utang Proyek/Retensi, Utang Dealer/Sekuritas, Beban Akrual, &amp; Utang Pajak</b>: Kewajiban operasional non-bunga kepada pemasok, kontraktor, dealer kendaraan, perusahaan efek/MI, beban masih harus dibayar, dan utang pajak (termasuk pajak tangguhan).</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan seluruh utang usaha, utang retensi, utang lain-lain, beban akrual, utang bunga/dividen, utang pajak, liabilitas pajak tangguhan, dan utang dealer/sekuritas.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan pembiayaan modal kerja gratis (tanpa bunga) yang diperoleh perusahaan dari pemasok, kontraktor, dan tenggat pembayaran beban/pajak.<br/><b>Saran Analisis:</b> Hitung <b>Days Payable Outstanding (DPO)</b>; DPO yang panjang bisa berarti daya tawar tinggi ke pemasok, namun jika disertai kas tipis bisa menandakan perusahaan kesulitan membayar vendor.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (22):</b><br/><code>+</code> <code>[L.C.20]</code> <code>TradePayablesThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.21]</code> <code>TradePayablesRelatedParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.22]</code> <code>OtherPayablesThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.23]</code> <code>OtherPayablesRelatedParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.24]</code> <code>DividendsPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.25]</code> <code>TaxesPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.17]</code> <code>DeferredTaxLiabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.26]</code> <code>ProjectPayables</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.27]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Retention<wbr>Payables</code> <i>[A1, B1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.28]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Joint<wbr>Operations<wbr>Liabilities</code> <i>[C1, E5, K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.29]</code> <code>CurrentDueToRelatedParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.30]</code> <code>CurrentDueToStockholders</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.31]</code> <code>CurrentAccruedExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.32]</code> <code>AccruedStrippingCosts</code> <i>[D2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.33]</code> <code>ExcisePayable</code> <i>[A1, D3]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.34]</code> <code>CurrentTaxAmnestyLiabilities</code> <i>[E5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.N.18]</code> <code>LongTermRetentionPayables</code> <i>[A1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.N.19]</code> <code>Long<wbr>Term<wbr>Joint<wbr>Operations<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.20]</code> <code>Long<wbr>Term<wbr>Electricity<wbr>Purchase<wbr>Payables</code> <i>[I1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.N.21]</code> <code>Non<wbr>Current<wbr>Due<wbr>To<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.22]</code> <code>NonCurrentDueToStockholders</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.23]</code> <code>Non<wbr>Current<wbr>Tax<wbr>Amnesty<wbr>Liabilities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (10):</b><br/><code>+</code> <code>[L.C.20]</code> <code>TradePayablesThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.21]</code> <code>TradePayablesRelatedParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.22]</code> <code>OtherPayablesThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.23]</code> <code>OtherPayablesRelatedParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.24]</code> <code>DividendsPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.25]</code> <code>TaxesPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.17]</code> <code>DeferredTaxLiabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.08]</code> <code>DueToRelatedParties</code> <i>[C2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.09]</code> <code>DueToStockholders</code> <i>[J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.10]</code> <code>AccruedExpenses</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>C1</code>, <code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code>, <code>J3</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (15):</b><br/><code>+</code> <code>[L.C.20]</code> <code>TradePayablesThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.21]</code> <code>TradePayablesRelatedParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.22]</code> <code>OtherPayablesThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.23]</code> <code>OtherPayablesRelatedParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.24]</code> <code>DividendsPayable</code> <i>[H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.25]</code> <code>TaxesPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.17]</code> <code>DeferredTaxLiabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.26]</code> <code>ProjectPayables</code> <i>[E3, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.27]</code> <code>Current<wbr>Maturities<wbr>Of<wbr>Retention<wbr>Payables</code> <i>[H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.29]</code> <code>CurrentDueToRelatedParties</code> <i>[H1, K1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.30]</code> <code>CurrentDueToStockholders</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.31]</code> <code>CurrentAccruedExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.18]</code> <code>LongTermRetentionPayables</code> <i>[J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.N.21]</code> <code>Non<wbr>Current<wbr>Due<wbr>To<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.22]</code> <code>NonCurrentDueToStockholders</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (5):</b><br/><code>+</code> <code>[L.C.20]</code> <code>TradePayablesThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.21]</code> <code>TradePayablesRelatedParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.25]</code> <code>TaxesPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.08]</code> <code>DueToRelatedParties</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.10]</code> <code>AccruedExpenses</code> <i>[H1, J2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>C</code>, <code>D</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>C1</code>, <code>D1</code>, <code>D2</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (16):</b><br/><code>+</code> <code>[L.C.20]</code> <code>TradePayablesThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.21]</code> <code>TradePayablesRelatedParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.22]</code> <code>OtherPayablesThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.23]</code> <code>OtherPayablesRelatedParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.24]</code> <code>DividendsPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.25]</code> <code>TaxesPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.17]</code> <code>DeferredTaxLiabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.26]</code> <code>ProjectPayables</code> <i>[J1, J2, J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.29]</code> <code>CurrentDueToRelatedParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.30]</code> <code>CurrentDueToStockholders</code> <i>[A1, J3, K1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.31]</code> <code>CurrentAccruedExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.19]</code> <code>Long<wbr>Term<wbr>Joint<wbr>Operations<wbr>Liabilities</code> <i>[J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.N.20]</code> <code>Long<wbr>Term<wbr>Electricity<wbr>Purchase<wbr>Payables</code> <i>[J4]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.N.21]</code> <code>Non<wbr>Current<wbr>Due<wbr>To<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.22]</code> <code>NonCurrentDueToStockholders</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.23]</code> <code>Non<wbr>Current<wbr>Tax<wbr>Amnesty<wbr>Liabilities</code> <i>[D1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (6):</b><br/><code>+</code> <code>[L.C.20]</code> <code>TradePayablesThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.22]</code> <code>OtherPayablesThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.25]</code> <code>TaxesPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.17]</code> <code>DeferredTaxLiabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.09]</code> <code>DueToStockholders</code> <i>[K1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.10]</code> <code>AccruedExpenses</code> <i>[J2, K1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (8):</b><br/><code>+</code> <code>[L.C.24]</code> <code>DividendsPayable</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.25]</code> <code>TaxesPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.17]</code> <code>DeferredTaxLiabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.10]</code> <code>AccruedExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.57]</code> <code>AccountsPayable</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.58]</code> <code>InterestPayables</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.59]</code> <code>DealerPayables</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.62]</code> <code>SecuritiesCompanyPayables</code> <i>[G5]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (8):</b><br/><code>+</code> <code>[L.C.24]</code> <code>DividendsPayable</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.25]</code> <code>TaxesPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.17]</code> <code>DeferredTaxLiabilities</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.08]</code> <code>DueToRelatedParties</code> <i>[C1, G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.10]</code> <code>AccruedExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.57]</code> <code>AccountsPayable</code> <i>[C1, G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.58]</code> <code>InterestPayables</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.59]</code> <code>DealerPayables</code> <i>[E6, G2, I2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[L.C.24]</code> <code>DividendsPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.25]</code> <code>TaxesPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.17]</code> <code>DeferredTaxLiabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.10]</code> <code>AccruedExpenses</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (7):</b><br/><code>+</code> <code>[L.C.24]</code> <code>DividendsPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.25]</code> <code>TaxesPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.17]</code> <code>DeferredTaxLiabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.10]</code> <code>AccruedExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.60]</code> <code>MarginPayables</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.61]</code> <code>PayablesToSecuritiesCompany</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.63]</code> <code>PayablesToInvestmentManagers</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>collective_investment_contract</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>B</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>B1</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[L.C.25]</code> <code>TaxesPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.10]</code> <code>AccruedExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.57]</code> <code>AccountsPayable</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.L.06]</code> <b><code>insurance_technical_reserves_and_claims</code></b> &nbsp;<span><i>(Total 15 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Cadangan Teknis Asuransi, Liabilitas Manfaat Polis, Liabilitas Unit-Link, &amp; Utang Klaim/Reasuransi</b>: Kewajiban kontrak asuransi (CAPYBMP, cadangan klaim/IBNR, manfaat polis masa depan), dana investasi pemegang polis <i>unit-linked</i>, serta utang klaim/reasuransi.</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan seluruh akun liabilitas kontrak asuransi, cadangan premi/klaim, liabilitas <i>unit-linked</i>, utang klaim/komisi/reasuransi/retrosesi, dan titipan premi.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan total kewajiban aktuaria dan cadangan klaim yang wajib disiapkan perusahaan asuransi untuk melindungi pemegang polis.<br/><b>Saran Analisis:</b> Pastikan nilai portofolio investasi likuid asuransi (<code>[CAN.BS.A.01] + [CAN.BS.A.03]</code>) selalu melebihi cadangan teknis ini (<i> Reserve Coverage &gt; 100%</i>).</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C3</code>, <code>E7</code>, <code>G5</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b> <code>all_variants</code><br/>• <code>current_and_non_current</code><br/>• <code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[L.C.39]</code> <code>LiabilitiesToPolicyholders</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.40]</code> <code>InsuranceContractLiabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.41]</code> <code>CoinsuranceLiabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.42]</code> <code>ReinsurancePayables</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G4</code>, <code>G5</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[L.C.40]</code> <code>InsuranceContractLiabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.67]</code> <code>InsurancePayables</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.69]</code> <code>Liabilities<wbr>To<wbr>Policyholder<wbr>In<wbr>Unit<wbr>Linked<wbr>Contracts</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G2</code>, <code>G5</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[L.C.40]</code> <code>InsuranceContractLiabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.67]</code> <code>InsurancePayables</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (12):</b><br/><code>+</code> <code>[L.C.41]</code> <code>CoinsuranceLiabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.42]</code> <code>ReinsurancePayables</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.64]</code> <code>ClaimPayables</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.65]</code> <code>CommissionPayables</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.66]</code> <code>RetrocessionPayables</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.68]</code> <code>PremiumDeposits</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.69]</code> <code>Liabilities<wbr>To<wbr>Policyholder<wbr>In<wbr>Unit<wbr>Linked<wbr>Contracts</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.70]</code> <code>Insurance<wbr>Liabilities<wbr>On<wbr>Unearned<wbr>Premium</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.71]</code> <code>Insurance<wbr>Liabilities<wbr>On<wbr>Estimated<wbr>Claims<wbr>Liability</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.72]</code> <code>Insurance<wbr>Liabilities<wbr>For<wbr>Future<wbr>Policy<wbr>Benefits</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.73]</code> <code>Insurance<wbr>Liabilities<wbr>On<wbr>Deferred<wbr>Premium<wbr>Income</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.74]</code> <code>Provisions<wbr>For<wbr>Losses<wbr>Arising<wbr>Resulting<wbr>From<wbr>Liability<wbr>Adequacy<wbr>Test</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.L.07]</code> <b><code>unearned_revenue_employee_benefits_and_provisions</code></b> &nbsp;<span><i>(Total 46 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Uang Muka Pelanggan (<i>Contract Liabilities</i>), Pendapatan Diterima di Muka, Liabilitas Imbalan Kerja, &amp; Provisi</b>: DP pesanan pelanggan/pembeli properti, pendapatan sewa diterima di muka, cadangan pesangon/pensiun karyawan (PSAK 24), provisi bongkar tambang, dan liabilitas lain-lain.</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan seluruh uang muka pelanggan, pendapatan diterima di muka, liabilitas imbalan pascakerja, provisi, estimasi kerugian komitmen/kontinjensi, dan liabilitas lain-lain.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan pesanan pelanggan yang uangnya sudah diterima di muka (<i>unearned revenue / down payment</i>) serta kewajiban imbalan kerja/pensiun karyawan.<br/><b>Saran Analisis:</b> Pada sektor Properti &amp; Konstruksi, kenaikan <b>Uang Muka Pelanggan</b> adalah sinyal positif karena mencerminkan tabungan pendapatan (<i>backlog</i>) yang tinggal menunggu serah terima.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (32):</b><br/><code>+</code> <code>[L.C.35]</code> <code>DueToCustomersThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.36]</code> <code>DueToCustomersRelatedParties</code> <i>[B1, J1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.37]</code> <code>Payables<wbr>To<wbr>Customers<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.38]</code> <code>Payables<wbr>To<wbr>Clearing<wbr>And<wbr>Settlement<wbr>Guarantee<wbr>Institution</code> <i>[98, C3, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.43]</code> <code>Liabilities<wbr>Directly<wbr>Associated<wbr>With<wbr>Non<wbr>Current<wbr>Assets<wbr>Or<wbr>Disposal<wbr>Groups<wbr>Classified<wbr>As<wbr>Held<wbr>For<wbr>Sale<wbr>Or<wbr>As<wbr>Held<wbr>For<wbr>Distribution<wbr>To<wbr>Owners</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.44]</code> <code>Current<wbr>Advances<wbr>From<wbr>Customers<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.45]</code> <code>Current<wbr>Advances<wbr>From<wbr>Customers<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.46]</code> <code>CurrentUnearnedRevenue</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.47]</code> <code>CurrentDeferredRevenue</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.48]</code> <code>CurrentContractLiabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.49]</code> <code>Payables<wbr>To<wbr>Customers<wbr>Related<wbr>Parties</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.50]</code> <code>Short<wbr>Term<wbr>Post<wbr>Employment<wbr>Benefit<wbr>Obligations</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.51]</code> <code>ShareBasedPaymentLiabilities</code> <i>[A1, B1, I1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.52]</code> <code>CurrentProvisionsForOverlay</code> <i>[C3]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.53]</code> <code>Current<wbr>Provisions<wbr>For<wbr>Restoration<wbr>And<wbr>Rehabilitation</code> <i>[A1, B1, E5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.54]</code> <code>Current<wbr>Provisions<wbr>For<wbr>Asset<wbr>Dismantling<wbr>Costs</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.55]</code> <code>OtherCurrentProvisions</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.56]</code> <code>OtherNonCurrentProvisions</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.57]</code> <code>Other<wbr>Current<wbr>Financial<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.58]</code> <code>Other<wbr>Non<wbr>Current<wbr>Financial<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.59]</code> <code>Other<wbr>Current<wbr>Non<wbr>Financial<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.60]</code> <code>Other<wbr>Non<wbr>Current<wbr>Non<wbr>Financial<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.24]</code> <code>Non<wbr>Current<wbr>Advances<wbr>From<wbr>Customers<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.25]</code> <code>Non<wbr>Current<wbr>Advances<wbr>From<wbr>Customers<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.26]</code> <code>NonCurrentUnearnedRevenue</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.27]</code> <code>NonCurrentDeferredRevenue</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.28]</code> <code>Non-Current<wbr>Contract<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.29]</code> <code>Long<wbr>Term<wbr>Post<wbr>Employment<wbr>Benefit<wbr>Obligations</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.30]</code> <code>Non<wbr>Current<wbr>Provisions<wbr>For<wbr>Overlay</code> <i>[C3]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.N.31]</code> <code>Non<wbr>Current<wbr>Provisions<wbr>For<wbr>Restoration<wbr>And<wbr>Rehabilitation</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.32]</code> <code>Non<wbr>Current<wbr>Provisions<wbr>For<wbr>Asset<wbr>Dismantling<wbr>Costs</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.33]</code> <code>Non<wbr>Current<wbr>Provisions<wbr>For<wbr>Infrastructure<wbr>Development<wbr>Public<wbr>And<wbr>Social<wbr>Facilities</code> <i>[E5]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (12):</b><br/><code>+</code> <code>[L.C.35]</code> <code>DueToCustomersThirdParties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.36]</code> <code>DueToCustomersRelatedParties</code> <i>[B1, J1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.37]</code> <code>Payables<wbr>To<wbr>Customers<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.38]</code> <code>Payables<wbr>To<wbr>Clearing<wbr>And<wbr>Settlement<wbr>Guarantee<wbr>Institution</code> <i>[98, C3, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.43]</code> <code>Liabilities<wbr>Directly<wbr>Associated<wbr>With<wbr>Non<wbr>Current<wbr>Assets<wbr>Or<wbr>Disposal<wbr>Groups<wbr>Classified<wbr>As<wbr>Held<wbr>For<wbr>Sale<wbr>Or<wbr>As<wbr>Held<wbr>For<wbr>Distribution<wbr>To<wbr>Owners</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.11]</code> <code>Advances<wbr>From<wbr>Customers<wbr>Third<wbr>Parties</code> <i>[E1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.12]</code> <code>UnearnedRevenue</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.13]</code> <code>DeferredRevenue</code> <i>[C2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.14]</code> <code>ContractLiabilities</code> <i>[E1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.15]</code> <code>Post<wbr>Employment<wbr>Benefit<wbr>Obligations</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.16]</code> <code>OtherFinancialLiabilities</code> <i>[E6, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.17]</code> <code>OtherNonFinancialLiabilities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>C1</code>, <code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code>, <code>J3</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (22):</b><br/><code>+</code> <code>[L.C.35]</code> <code>DueToCustomersThirdParties</code> <i>[H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.36]</code> <code>DueToCustomersRelatedParties</code> <i>[J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.43]</code> <code>Liabilities<wbr>Directly<wbr>Associated<wbr>With<wbr>Non<wbr>Current<wbr>Assets<wbr>Or<wbr>Disposal<wbr>Groups<wbr>Classified<wbr>As<wbr>Held<wbr>For<wbr>Sale<wbr>Or<wbr>As<wbr>Held<wbr>For<wbr>Distribution<wbr>To<wbr>Owners</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.44]</code> <code>Current<wbr>Advances<wbr>From<wbr>Customers<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.45]</code> <code>Current<wbr>Advances<wbr>From<wbr>Customers<wbr>Related<wbr>Parties</code> <i>[G5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.46]</code> <code>CurrentUnearnedRevenue</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.47]</code> <code>CurrentDeferredRevenue</code> <i>[C1, E5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.48]</code> <code>CurrentContractLiabilities</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.50]</code> <code>Short<wbr>Term<wbr>Post<wbr>Employment<wbr>Benefit<wbr>Obligations</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.55]</code> <code>OtherCurrentProvisions</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.56]</code> <code>OtherNonCurrentProvisions</code> <i>[E5, H1, J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.57]</code> <code>Other<wbr>Current<wbr>Financial<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.58]</code> <code>Other<wbr>Non<wbr>Current<wbr>Financial<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.59]</code> <code>Other<wbr>Current<wbr>Non<wbr>Financial<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.60]</code> <code>Other<wbr>Non<wbr>Current<wbr>Non<wbr>Financial<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.24]</code> <code>Non<wbr>Current<wbr>Advances<wbr>From<wbr>Customers<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.25]</code> <code>Non<wbr>Current<wbr>Advances<wbr>From<wbr>Customers<wbr>Related<wbr>Parties</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.N.26]</code> <code>NonCurrentUnearnedRevenue</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.27]</code> <code>NonCurrentDeferredRevenue</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.28]</code> <code>Non-Current<wbr>Contract<wbr>Liabilities</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.N.29]</code> <code>Long<wbr>Term<wbr>Post<wbr>Employment<wbr>Benefit<wbr>Obligations</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.33]</code> <code>Non<wbr>Current<wbr>Provisions<wbr>For<wbr>Infrastructure<wbr>Development<wbr>Public<wbr>And<wbr>Social<wbr>Facilities</code> <i>[H1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (5):</b><br/><code>+</code> <code>[L.L.12]</code> <code>UnearnedRevenue</code> <i>[J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.13]</code> <code>DeferredRevenue</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.15]</code> <code>Post<wbr>Employment<wbr>Benefit<wbr>Obligations</code> <i>[H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.16]</code> <code>OtherFinancialLiabilities</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.75]</code> <code>AdvancesFromCustomers</code> <i>[H1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>C</code>, <code>D</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>C1</code>, <code>D1</code>, <code>D2</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (19):</b><br/><code>+</code> <code>[L.C.43]</code> <code>Liabilities<wbr>Directly<wbr>Associated<wbr>With<wbr>Non<wbr>Current<wbr>Assets<wbr>Or<wbr>Disposal<wbr>Groups<wbr>Classified<wbr>As<wbr>Held<wbr>For<wbr>Sale<wbr>Or<wbr>As<wbr>Held<wbr>For<wbr>Distribution<wbr>To<wbr>Owners</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.44]</code> <code>Current<wbr>Advances<wbr>From<wbr>Customers<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.45]</code> <code>Current<wbr>Advances<wbr>From<wbr>Customers<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.46]</code> <code>CurrentUnearnedRevenue</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.47]</code> <code>CurrentDeferredRevenue</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.48]</code> <code>CurrentContractLiabilities</code> <i>[A1, K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.50]</code> <code>Short<wbr>Term<wbr>Post<wbr>Employment<wbr>Benefit<wbr>Obligations</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.52]</code> <code>CurrentProvisionsForOverlay</code> <i>[J1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.55]</code> <code>OtherCurrentProvisions</code> <i>[J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.56]</code> <code>OtherNonCurrentProvisions</code> <i>[A1, J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.C.57]</code> <code>Other<wbr>Current<wbr>Financial<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.58]</code> <code>Other<wbr>Non<wbr>Current<wbr>Financial<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.59]</code> <code>Other<wbr>Current<wbr>Non<wbr>Financial<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.60]</code> <code>Other<wbr>Non<wbr>Current<wbr>Non<wbr>Financial<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.26]</code> <code>NonCurrentUnearnedRevenue</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.27]</code> <code>NonCurrentDeferredRevenue</code> <i>[J1, J3, K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.N.28]</code> <code>Non-Current<wbr>Contract<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.29]</code> <code>Long<wbr>Term<wbr>Post<wbr>Employment<wbr>Benefit<wbr>Obligations</code> &nbsp;·&nbsp; <code>+</code> <code>[L.N.30]</code> <code>Non<wbr>Current<wbr>Provisions<wbr>For<wbr>Overlay</code> <i>[J1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[L.L.12]</code> <code>UnearnedRevenue</code> <i>[K1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.15]</code> <code>Post<wbr>Employment<wbr>Benefit<wbr>Obligations</code> <i>[J2, K1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (6):</b><br/><code>+</code> <code>[L.L.15]</code> <code>Post<wbr>Employment<wbr>Benefit<wbr>Obligations</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.76]</code> <code>AdvancesAndInstallments</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.77]</code> <code>DeferredIncome</code> <i>[G1, G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.78]</code> <code>Estimated<wbr>Losses<wbr>On<wbr>Commitments<wbr>And<wbr>Contingencies</code> <i>[G1, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.79]</code> <code>Provisions</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.81]</code> <code>OtherLiabilities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (7):</b><br/><code>+</code> <code>[L.L.14]</code> <code>ContractLiabilities</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.15]</code> <code>Post<wbr>Employment<wbr>Benefit<wbr>Obligations</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.16]</code> <code>OtherFinancialLiabilities</code> <i>[C1, G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.76]</code> <code>AdvancesAndInstallments</code> <i>[C1, G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.77]</code> <code>DeferredIncome</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.79]</code> <code>Provisions</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[L.L.81]</code> <code>OtherLiabilities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[L.L.14]</code> <code>ContractLiabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.15]</code> <code>Post<wbr>Employment<wbr>Benefit<wbr>Obligations</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.80]</code> <code>ZakatInstance</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.81]</code> <code>OtherLiabilities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (6):</b><br/><code>+</code> <code>[L.C.37]</code> <code>Payables<wbr>To<wbr>Customers<wbr>Third<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.38]</code> <code>Payables<wbr>To<wbr>Clearing<wbr>And<wbr>Settlement<wbr>Guarantee<wbr>Institution</code> &nbsp;·&nbsp; <code>+</code> <code>[L.C.49]</code> <code>Payables<wbr>To<wbr>Customers<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.14]</code> <code>ContractLiabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.15]</code> <code>Post<wbr>Employment<wbr>Benefit<wbr>Obligations</code> &nbsp;·&nbsp; <code>+</code> <code>[L.L.81]</code> <code>OtherLiabilities</code></td>
    </tr>
  </tbody>
</table>

### 1.3 Ekuitas & Aset Neto Kanonik (`[CAN.BS.E]`)

<table width="100%">
  <colgroup>
    <col width="34%" />
    <col width="34%" />
    <col width="32%" />
  </colgroup>
  <thead>
    <tr>
      <th align="left" width="34%">Penjelasan / Entry Points / Variant</th>
      <th align="left" width="34%">Aturan Agregasi / Sectors / Accounts</th>
      <th align="left" width="32%">Makna Ekonomi &amp; Saran Analisis / Subsectors</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="3"><code>[CAN.BS.E]</code> <b><code>total_equity_or_net_assets</code></b> &nbsp;<span><i>(Total 5 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Total Ekuitas Konsolidasi / Jumlah Aset Neto KIK</b>: Total kekayaan bersih perusahaan (Ekuitas Pemilik Induk + Kepentingan Nonpengendali, atau Aset Neto pada KIK/DIRE).</td>
      <td width="34%" valign="top"><b>Coalesce Priority</b>: <code>coalesce(Equity, NetAssets, NetAssetsAttributableToParticipationUnitHolders)</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan <b>bantalan modal sendiri (<i>solvency cushion</i>)</b> yang menyerap potensi kerugian sebelum menyentuh dana kreditur.<br/><b>Saran Analisis:</b> Penyebut utama dalam rasio <b>Total DER</b>. Ekuitas yang bernilai negatif (<i>Defisiensi Modal</i>) menandakan perusahaan secara teknis insolven.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code>, <code>property</code>, <code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b> <code>all_variants</code><br/>• <code>current_and_non_current</code><br/>• <code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[E]</code> <code>Equity</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code>, <code>financing</code>, <code>insurance</code>, <code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>C1</code>, <code>E6</code>, <code>G1</code>, <code>G2</code>, <code>G3</code>, <code>G4</code>, <code>G5</code>, <code>H1</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[E]</code> <code>Equity</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>collective_investment_contract</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>B</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>B1</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[NA]</code> <code>NetAssets</code> &nbsp;·&nbsp; <code>+</code> <code>[NA.U]</code> <code>Net<wbr>Assets<wbr>Attributable<wbr>To<wbr>Participation<wbr>Unit<wbr>Holders</code> &nbsp;·&nbsp; <code>+</code> <code>[NA.NAV]</code> <code>Net<wbr>Assets<wbr>Attributable<wbr>To<wbr>Unit<wbr>Holders<wbr>Per<wbr>Investment<wbr>Unit</code> &nbsp;·&nbsp; <code>+</code> <code>[NA.SH]</code> <code>OutstandingInvestmentUnits</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.E.P]</code> <b><code>equity_attributable_to_parent</code></b> &nbsp;<span><i>(Total 1 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Ekuitas yang Dapat Diatribusikan kepada Pemilik Entitas Induk</b>: Kekayaan bersih murni milik pemegang saham emiten induk (tidak termasuk hak minoritas anak usaha).</td>
      <td width="34%" valign="top"><b>Coalesce Priority</b>: <code>coalesce(EquityAttributableToEquityOwnersOfParentEntity, Equity − NonControllingInterests, NetAssets)</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan nilai kekayaan bersih (<i>Book Value</i>) yang benar-benar menjadi hak pemegang saham publik dan pengendali emiten induk.<br/><b>Saran Analisis:</b> Gunakan sebagai penyebut standar untuk menghitung <b>ROE</b> (<code>net_income_attributable_to_parent / equity_attributable_to_parent</code>) dan <b>PBV</b>.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code>, <code>property</code>, <code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b> <code>all_variants</code><br/>• <code>current_and_non_current</code><br/>• <code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[E.P]</code> <code>Equity<wbr>Attributable<wbr>To<wbr>Equity<wbr>Owners<wbr>Of<wbr>Parent<wbr>Entity</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code>, <code>financing</code>, <code>insurance</code>, <code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>C1</code>, <code>E6</code>, <code>G1</code>, <code>G2</code>, <code>G3</code>, <code>G4</code>, <code>G5</code>, <code>H1</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[E.P]</code> <code>Equity<wbr>Attributable<wbr>To<wbr>Equity<wbr>Owners<wbr>Of<wbr>Parent<wbr>Entity</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.E.NCI]</code> <b><code>non_controlling_interests_equity</code></b> &nbsp;<span><i>(Total 1 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Kepentingan Nonpengendali (<i>Minority Interest</i>) di Ekuitas</b>: Bagian kekayaan bersih anak-anak perusahaan yang dimiliki oleh pihak ketiga minoritas.</td>
      <td width="34%" valign="top"><b>Direct</b>: Ambil dari <code>[E.NCI] NonControllingInterests</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan seberapa besar porsi aset bersih anak-anak perusahaan yang sebenarnya dimiliki oleh mitra minoritas di luar pemegang saham induk.<br/><b>Saran Analisis:</b> Jika porsi NCI sangat besar, hati-hati membaca kas dan EBITDA konsolidasi karena sebagian milik pemegang saham minoritas anak usaha.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code>, <code>property</code>, <code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b> <code>all_variants</code><br/>• <code>current_and_non_current</code><br/>• <code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[E.NCI]</code> <code>NonControllingInterests</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code>, <code>financing</code>, <code>insurance</code>, <code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G1</code>, <code>G2</code>, <code>G3</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[E.NCI]</code> <code>NonControllingInterests</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.LE]</code> <b><code>total_liabilities_and_equity_check</code></b> &nbsp;<span><i>(Total 4 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Total Liabilitas, Dana Syirkah/Tabarru', dan Ekuitas (Total Pasiva)</b>: Jumlah akhir sisi pasiva neraca untuk validasi keseimbangan akuntansi.</td>
      <td width="34%" valign="top"><b>Coalesce Priority</b>: <code>coalesce(LiabilitiesAndEquity, LiabilitiesTemporarySyirkahFundsAndEquity, LiabilitiesTabarruFundsAndEquity, LiabilitiesAndNetAssets)</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan total sumber pendanaan perusahaan (Utang + Dana Syirkah + Modal Sendiri) yang membiayai seluruh Aset.<br/><b>Saran Analisis:</b> <b>Kontrol Validasi Pipeline:</b> Nilai akun ini wajib selalu sama persis (selisih = 0) dengan <code>total_assets</code>.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code>, <code>property</code>, <code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b> <code>all_variants</code><br/>• <code>current_and_non_current</code><br/>• <code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[LE]</code> <code>LiabilitiesAndEquity</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[LSE]</code> <code>Liabilities<wbr>Temporary<wbr>Syirkah<wbr>Funds<wbr>And<wbr>Equity</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code>, <code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G2</code>, <code>G3</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[LE]</code> <code>LiabilitiesAndEquity</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[LTE]</code> <code>Liabilities<wbr>Tabarru<wbr>Funds<wbr>And<wbr>Equity</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>collective_investment_contract</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>B</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>B1</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[LNA]</code> <code>LiabilitiesAndNetAssets</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.E.01]</code> <b><code>paid_in_capital_and_treasury_stock</code></b> &nbsp;<span><i>(Total 8 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Modal Disetor, Tambahan Modal Disetor (Agio Saham), &amp; Saham Treasuri</b>: Total modal saham biasa/preferen, agio saham (<i>additional paid-in capital</i>), uang muka setoran modal, dan opsi saham dikurangi saham treasuri (<i>buyback</i>).</td>
      <td width="34%" valign="top"><b>Sum (Net of Treasury Stock)</b>: Jumlahkan seluruh modal saham, <code>AdditionalPaidInCapital</code>, komponen ekuitas lainnya, dikurangi <code>TreasuryStocks</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan total modal uang tunai kumulatif yang disetorkan oleh pemegang saham (IPO, <i>Rights Issue</i>, <i>Private Placement</i>) dikurangi pembelian kembali saham (<i>Treasury Stock</i>).<br/><b>Saran Analisis:</b> Bandingkan dengan <code>retained_earnings_and_reserves</code> untuk melihat apakah ekuitas perusahaan tumbuh dari hasil laba bisnis atau sekadar suntikan modal berulang.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (8):</b><br/><code>+</code> <code>[E.P.01]</code> <code>CommonStocks</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.02]</code> <code>AdditionalPaidInCapital</code> &nbsp;·&nbsp; <code>−</code> <code>[E.P.04]</code> <code>TreasuryStocks</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.14]</code> <code>OtherComponentsOfEquity</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.15]</code> <code>PreferredStocks</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.18]</code> <code>StockOptions</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.19]</code> <code>Difference<wbr>Due<wbr>To<wbr>Changes<wbr>Of<wbr>Equity<wbr>In<wbr>Subsidiary<wbr>Associates</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.20]</code> <code>ProformaEquity</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[E.P.01]</code> <code>CommonStocks</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.02]</code> <code>AdditionalPaidInCapital</code> &nbsp;·&nbsp; <code>−</code> <code>[E.P.04]</code> <code>TreasuryStocks</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.14]</code> <code>OtherComponentsOfEquity</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>C1</code>, <code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code>, <code>J3</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (7):</b><br/><code>+</code> <code>[E.P.01]</code> <code>CommonStocks</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.02]</code> <code>AdditionalPaidInCapital</code> &nbsp;·&nbsp; <code>−</code> <code>[E.P.04]</code> <code>TreasuryStocks</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.14]</code> <code>OtherComponentsOfEquity</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.18]</code> <code>StockOptions</code> <i>[E5, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.19]</code> <code>Difference<wbr>Due<wbr>To<wbr>Changes<wbr>Of<wbr>Equity<wbr>In<wbr>Subsidiary<wbr>Associates</code> <i>[C1, E5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.20]</code> <code>ProformaEquity</code> <i>[G5, H1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[E.P.01]</code> <code>CommonStocks</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.02]</code> <code>AdditionalPaidInCapital</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.14]</code> <code>OtherComponentsOfEquity</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>C</code>, <code>D</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>C1</code>, <code>D1</code>, <code>D2</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (8):</b><br/><code>+</code> <code>[E.P.01]</code> <code>CommonStocks</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.02]</code> <code>AdditionalPaidInCapital</code> &nbsp;·&nbsp; <code>−</code> <code>[E.P.04]</code> <code>TreasuryStocks</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.14]</code> <code>OtherComponentsOfEquity</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.15]</code> <code>PreferredStocks</code> <i>[J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.18]</code> <code>StockOptions</code> <i>[J3, K1]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.19]</code> <code>Difference<wbr>Due<wbr>To<wbr>Changes<wbr>Of<wbr>Equity<wbr>In<wbr>Subsidiary<wbr>Associates</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.20]</code> <code>ProformaEquity</code> <i>[A1, J2, J3]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (5):</b><br/><code>+</code> <code>[E.P.01]</code> <code>CommonStocks</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.02]</code> <code>AdditionalPaidInCapital</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.14]</code> <code>OtherComponentsOfEquity</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.18]</code> <code>StockOptions</code> <i>[J3, K1]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.19]</code> <code>Difference<wbr>Due<wbr>To<wbr>Changes<wbr>Of<wbr>Equity<wbr>In<wbr>Subsidiary<wbr>Associates</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (7):</b><br/><code>+</code> <code>[E.P.01]</code> <code>CommonStocks</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.02]</code> <code>AdditionalPaidInCapital</code> &nbsp;·&nbsp; <code>−</code> <code>[E.P.04]</code> <code>TreasuryStocks</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.14]</code> <code>OtherComponentsOfEquity</code> <i>[G1, G5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.18]</code> <code>StockOptions</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.19]</code> <code>Difference<wbr>Due<wbr>To<wbr>Changes<wbr>Of<wbr>Equity<wbr>In<wbr>Subsidiary<wbr>Associates</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.20]</code> <code>ProformaEquity</code> <i>[G1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (6):</b><br/><code>+</code> <code>[E.P.01]</code> <code>CommonStocks</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.02]</code> <code>AdditionalPaidInCapital</code> &nbsp;·&nbsp; <code>−</code> <code>[E.P.04]</code> <code>TreasuryStocks</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.14]</code> <code>OtherComponentsOfEquity</code> <i>[C1, G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.18]</code> <code>StockOptions</code> <i>[C1]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.19]</code> <code>Difference<wbr>Due<wbr>To<wbr>Changes<wbr>Of<wbr>Equity<wbr>In<wbr>Subsidiary<wbr>Associates</code> <i>[G2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (5):</b><br/><code>+</code> <code>[E.P.01]</code> <code>CommonStocks</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.02]</code> <code>AdditionalPaidInCapital</code> &nbsp;·&nbsp; <code>−</code> <code>[E.P.04]</code> <code>TreasuryStocks</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.14]</code> <code>OtherComponentsOfEquity</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.19]</code> <code>Difference<wbr>Due<wbr>To<wbr>Changes<wbr>Of<wbr>Equity<wbr>In<wbr>Subsidiary<wbr>Associates</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[E.P.01]</code> <code>CommonStocks</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.02]</code> <code>AdditionalPaidInCapital</code> &nbsp;·&nbsp; <code>−</code> <code>[E.P.04]</code> <code>TreasuryStocks</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.14]</code> <code>OtherComponentsOfEquity</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.BS.E.02]</code> <b><code>retained_earnings_and_reserves</code></b> &nbsp;<span><i>(Total 15 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Saldo Laba Ditahan (<i>Retained Earnings</i>) &amp; Cadangan Akumulasi OCI</b>: Akumulasi laba bersih historis yang tidak dibagikan sebagai dividen (ditentukan maupun belum ditentukan penggunaannya) ditambah cadangan selisih kurs translasi, revaluasi aset, dan nilai wajar FVOCI.</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan <code>AppropriatedRetainedEarnings</code>, <code>UnappropriatedRetainedEarnings</code>, cadangan umum/wajib, dan seluruh akun <code>ReserveOf...</code> / <code>RevaluationReserves</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan <b>akumulasi sejarah penciptaan nilai (laba bersih dikurangi dividen)</b> sejak perusahaan berdiri.<br/><b>Saran Analisis:</b> Saldo laba yang tebal menunjukkan bisnis yang matang dan menguntungkan; sebaliknya saldo laba negatif (<i>Defisit</i>) adalah komponen penghukum berat dalam rumus <b>Altman Z-Score</b>.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (12):</b><br/><code>+</code> <code>[E.P.03]</code> <code>AdvancesInCapitalStock</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.05]</code> <code>Unappropriated<wbr>Retained<wbr>Earnings</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.06]</code> <code>AppropriatedRetainedEarnings</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.07]</code> <code>Reserve<wbr>Of<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.08]</code> <code>Reserve<wbr>For<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.09]</code> <code>Reserve<wbr>For<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.10]</code> <code>Reserve<wbr>Of<wbr>Gains<wbr>Losses<wbr>From<wbr>Investments<wbr>In<wbr>Equity<wbr>Instruments</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.11]</code> <code>Reserve<wbr>Of<wbr>Remeasurements<wbr>Of<wbr>Defined<wbr>Benefit<wbr>Plans</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.12]</code> <code>ReserveOfShareBasedPayments</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.13]</code> <code>OtherReserves</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.16]</code> <code>RevaluationReserves</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.17]</code> <code>ReserveOfCashFlowHedges</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (10):</b><br/><code>+</code> <code>[E.P.03]</code> <code>AdvancesInCapitalStock</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.05]</code> <code>Unappropriated<wbr>Retained<wbr>Earnings</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.06]</code> <code>AppropriatedRetainedEarnings</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.07]</code> <code>Reserve<wbr>Of<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.08]</code> <code>Reserve<wbr>For<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.09]</code> <code>Reserve<wbr>For<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.10]</code> <code>Reserve<wbr>Of<wbr>Gains<wbr>Losses<wbr>From<wbr>Investments<wbr>In<wbr>Equity<wbr>Instruments</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.11]</code> <code>Reserve<wbr>Of<wbr>Remeasurements<wbr>Of<wbr>Defined<wbr>Benefit<wbr>Plans</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.12]</code> <code>ReserveOfShareBasedPayments</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.13]</code> <code>OtherReserves</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>C1</code>, <code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code>, <code>J3</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (11):</b><br/><code>+</code> <code>[E.P.03]</code> <code>AdvancesInCapitalStock</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.05]</code> <code>Unappropriated<wbr>Retained<wbr>Earnings</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.06]</code> <code>AppropriatedRetainedEarnings</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.07]</code> <code>Reserve<wbr>Of<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.09]</code> <code>Reserve<wbr>For<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.10]</code> <code>Reserve<wbr>Of<wbr>Gains<wbr>Losses<wbr>From<wbr>Investments<wbr>In<wbr>Equity<wbr>Instruments</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.11]</code> <code>Reserve<wbr>Of<wbr>Remeasurements<wbr>Of<wbr>Defined<wbr>Benefit<wbr>Plans</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.12]</code> <code>ReserveOfShareBasedPayments</code> <i>[J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.13]</code> <code>OtherReserves</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.16]</code> <code>RevaluationReserves</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.17]</code> <code>ReserveOfCashFlowHedges</code> <i>[H1, J2, K1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[E.P.05]</code> <code>Unappropriated<wbr>Retained<wbr>Earnings</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.06]</code> <code>AppropriatedRetainedEarnings</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>C</code>, <code>D</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>C1</code>, <code>D1</code>, <code>D2</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>current_and_non_current</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (13):</b><br/><code>+</code> <code>[E.P.03]</code> <code>AdvancesInCapitalStock</code> <i>[A1, J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.05]</code> <code>Unappropriated<wbr>Retained<wbr>Earnings</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.06]</code> <code>AppropriatedRetainedEarnings</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.07]</code> <code>Reserve<wbr>Of<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.08]</code> <code>Reserve<wbr>For<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.09]</code> <code>Reserve<wbr>For<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.10]</code> <code>Reserve<wbr>Of<wbr>Gains<wbr>Losses<wbr>From<wbr>Investments<wbr>In<wbr>Equity<wbr>Instruments</code> <i>[A1, J1, J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.11]</code> <code>Reserve<wbr>Of<wbr>Remeasurements<wbr>Of<wbr>Defined<wbr>Benefit<wbr>Plans</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.12]</code> <code>ReserveOfShareBasedPayments</code> <i>[J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.13]</code> <code>OtherReserves</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.16]</code> <code>RevaluationReserves</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.17]</code> <code>ReserveOfCashFlowHedges</code> <i>[J1, J3, K1]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.23]</code> <code>TranslationAdjustment</code> <i>[J1, J4]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[E.P.05]</code> <code>Unappropriated<wbr>Retained<wbr>Earnings</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.06]</code> <code>AppropriatedRetainedEarnings</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.08]</code> <code>Reserve<wbr>For<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Financial<wbr>Assets</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (13):</b><br/><code>+</code> <code>[E.P.03]</code> <code>AdvancesInCapitalStock</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.05]</code> <code>Unappropriated<wbr>Retained<wbr>Earnings</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.07]</code> <code>Reserve<wbr>Of<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.08]</code> <code>Reserve<wbr>For<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.09]</code> <code>Reserve<wbr>For<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets</code> <i>[G1, G4, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.10]</code> <code>Reserve<wbr>Of<wbr>Gains<wbr>Losses<wbr>From<wbr>Investments<wbr>In<wbr>Equity<wbr>Instruments</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.11]</code> <code>Reserve<wbr>Of<wbr>Remeasurements<wbr>Of<wbr>Defined<wbr>Benefit<wbr>Plans</code> <i>[G1, G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.12]</code> <code>ReserveOfShareBasedPayments</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.13]</code> <code>OtherReserves</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.16]</code> <code>RevaluationReserves</code> <i>[G1, G5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.17]</code> <code>ReserveOfCashFlowHedges</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.21]</code> <code>GeneralAndLegalReserves</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.22]</code> <code>SpecificReserves</code> <i>[G1, G2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (10):</b><br/><code>+</code> <code>[E.P.05]</code> <code>Unappropriated<wbr>Retained<wbr>Earnings</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.07]</code> <code>Reserve<wbr>Of<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.08]</code> <code>Reserve<wbr>For<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Financial<wbr>Assets</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.09]</code> <code>Reserve<wbr>For<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.10]</code> <code>Reserve<wbr>Of<wbr>Gains<wbr>Losses<wbr>From<wbr>Investments<wbr>In<wbr>Equity<wbr>Instruments</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.11]</code> <code>Reserve<wbr>Of<wbr>Remeasurements<wbr>Of<wbr>Defined<wbr>Benefit<wbr>Plans</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.13]</code> <code>OtherReserves</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.16]</code> <code>RevaluationReserves</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.17]</code> <code>ReserveOfCashFlowHedges</code> <i>[E6, G2, I2]</i> &nbsp;·&nbsp; <code>+</code> <code>[E.P.21]</code> <code>GeneralAndLegalReserves</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (9):</b><br/><code>+</code> <code>[E.P.05]</code> <code>Unappropriated<wbr>Retained<wbr>Earnings</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.06]</code> <code>AppropriatedRetainedEarnings</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.07]</code> <code>Reserve<wbr>Of<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.08]</code> <code>Reserve<wbr>For<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.09]</code> <code>Reserve<wbr>For<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.10]</code> <code>Reserve<wbr>Of<wbr>Gains<wbr>Losses<wbr>From<wbr>Investments<wbr>In<wbr>Equity<wbr>Instruments</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.11]</code> <code>Reserve<wbr>Of<wbr>Remeasurements<wbr>Of<wbr>Defined<wbr>Benefit<wbr>Plans</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.13]</code> <code>OtherReserves</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.16]</code> <code>RevaluationReserves</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>liquidity</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[E.P.05]</code> <code>Unappropriated<wbr>Retained<wbr>Earnings</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.06]</code> <code>AppropriatedRetainedEarnings</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.11]</code> <code>Reserve<wbr>Of<wbr>Remeasurements<wbr>Of<wbr>Defined<wbr>Benefit<wbr>Plans</code> &nbsp;·&nbsp; <code>+</code> <code>[E.P.13]</code> <code>OtherReserves</code></td>
    </tr>
  </tbody>
</table>

---

## 2. Pemetaan Kanonik Laba Rugi (`income_statement` — 17 Akun Kanonik dari 201 Akun Mentah)

### 2.1 Pendapatan, Beban Pokok, & Pendapatan Operasional Bersih (`[CAN.IS.REV]` & `[CAN.IS.GP]`)

<table width="100%">
  <colgroup>
    <col width="34%" />
    <col width="34%" />
    <col width="32%" />
  </colgroup>
  <thead>
    <tr>
      <th align="left" width="34%">Penjelasan / Entry Points / Variant</th>
      <th align="left" width="34%">Aturan Agregasi / Sectors / Accounts</th>
      <th align="left" width="32%">Makna Ekonomi &amp; Saran Analisis / Subsectors</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="3"><code>[CAN.IS.REV.01]</code> <b><code>gross_revenue_real_sector</code></b> &nbsp;<span><i>(Total 1 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Pendapatan Usaha &amp; Penjualan Bruto Sektor Riil</b>: Total omzet penjualan barang, pendapatan jasa, pendapatan konstruksi/konsesi jalan tol, serta pendapatan penjualan &amp; sewa properti/hotel.</td>
      <td width="34%" valign="top"><b>Direct Anchor</b>: Ambil langsung dari <code>[PL.C.EBT.GP.01] SalesAndRevenue</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan daya serap pasar, volume aktivitas bisnis, dan pangsa pasar (<i>market share</i>) perusahaan sektor riil.<br/><b>Saran Analisis:</b> Pantau pertumbuhan omzet (<b>Revenue Growth YoY / QoQ</b>) dan bandingkan dengan arus kas masuk pelanggan (<code>[CAN.CF.CFO.01]</code>) untuk menguji kualitas pendapatan.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code>, <code>property</code>, <code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b> <code>all_variants</code><br/>• <code>by_function_after_tax</code><br/>• <code>by_function_before_tax</code><br/>• <code>by_nature_after_tax</code><br/>• <code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[PL.C.EBT.GP.01]</code> <code>SalesAndRevenue</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.IS.REV.02]</code> <b><code>cost_of_revenue_real_sector</code></b> &nbsp;<span><i>(Total 3 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Harga Pokok Penjualan (HPP / <i>Cost of Goods Sold</i>) &amp; Beban Pokok Properti/Konstruksi</b>: Biaya produksi/pengadaan langsung atas barang dan jasa yang terjual, termasuk beban pokok tanah properti dan beban rekayasa/konstruksi.</td>
      <td width="34%" valign="top"><b>Coalesce / Sum</b>: Ambil dari <code>CostOfSalesAndRevenue</code> (pada varian <i>By Function</i>) ditambah <code>CostOfLand</code> dan <code>ConstructionEngineeringAndProcurementExpenses</code> jika disajikan terpisah.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan biaya langsung untuk memproduksi barang atau menyelesaikan proyek/jasa sebelum dikurangi biaya operasional kantor.<br/><b>Saran Analisis:</b> Kurangkan dari <code>gross_revenue_real_sector</code> untuk menguji kekuatan penentuan harga jual (<i>pricing power</i>) lewat <b>Gross Profit Margin (GPM)</b>.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code>, <code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_function_after_tax</code><br/>• <code>by_function_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>−</code> <code>[PL.C.EBT.GP.02]</code> <code>CostOfSalesAndRevenue</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>C1</code>, <code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code>, <code>J3</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_function_after_tax</code><br/>• <code>by_function_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>−</code> <code>[PL.C.EBT.GP.02]</code> <code>CostOfSalesAndRevenue</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>−</code> <code>[PL.C.EBT.GP.38]</code> <code>CostOfLand</code> <i>[H1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>−</code> <code>[PL.C.EBT.GP.38]</code> <code>CostOfLand</code> <i>[H1]</i> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.GP.39]</code> <code>Construction<wbr>Engineering<wbr>And<wbr>Procurement<wbr>Expenses</code> <i>[H1]</i></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.IS.REV.03]</code> <b><code>banking_and_multifinance_operating_revenue</code></b> &nbsp;<span><i>(Total 16 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Pendapatan Bunga, Bagi Hasil Syariah, Provisi, &amp; Pembiayaan Multifinance</b>: Pendapatan bunga kredit/SBN, pendapatan pengelolaan dana mudharib, komisi/provisi non-kredit, serta pendapatan pembiayaan konsumen, sewa pembiayaan (<i>finance/operating lease</i>), <i>factoring</i>, murabahah, ijarah, dan administrasi dikurangi bagi hasil dana syirkah temporer.</td>
      <td width="34%" valign="top"><b>Sum (Net of Syirkah Return)</b>: Jumlahkan seluruh pendapatan bunga, syariah, dan pembiayaan multifinance dikurangi <code>ThirdPartiesShareOnReturnOfTemporarySyirkahFunds</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan daya cetak pendapatan bunga, bagi hasil syariah, dan sewa pembiayaan dari portofolio aset produktif Bank &amp; Multifinance.<br/><b>Saran Analisis:</b> Kurangkan dengan beban bunga pendanaan (<code>InterestExpenses</code> di <code>[CAN.IS.FIN]</code>) untuk memperoleh <b>Net Interest Income (NII)</b> dan menghitung <b>NIM</b>.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G5</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (5):</b><br/><code>+</code> <code>[PL.C.EBT.GP.04]</code> <code>Revenue<wbr>From<wbr>Fund<wbr>Management<wbr>As<wbr>Mudharib</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.GP.05]</code> <code>Third<wbr>Parties<wbr>Share<wbr>On<wbr>Return<wbr>Of<wbr>Temporary<wbr>Syirkah<wbr>Funds</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.06]</code> <code>Provisions<wbr>And<wbr>Commissions<wbr>Income<wbr>From<wbr>Transactions<wbr>Other<wbr>Than<wbr>Loan</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.08]</code> <code>RevenueFromConsumerFinancing</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.10]</code> <code>RevenueFromFinanceLease</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[PL.C.EBT.GP.04]</code> <code>Revenue<wbr>From<wbr>Fund<wbr>Management<wbr>As<wbr>Mudharib</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.GP.05]</code> <code>Third<wbr>Parties<wbr>Share<wbr>On<wbr>Return<wbr>Of<wbr>Temporary<wbr>Syirkah<wbr>Funds</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.06]</code> <code>Provisions<wbr>And<wbr>Commissions<wbr>Income<wbr>From<wbr>Transactions<wbr>Other<wbr>Than<wbr>Loan</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (10):</b><br/><code>+</code> <code>[PL.C.EBT.GP.03]</code> <code>InterestAndFinanceIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.07]</code> <code>IncomeFromConsumerFinancing</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.09]</code> <code>IncomeFromFinanceLease</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.11]</code> <code>IncomeFromOperatingLease</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.12]</code> <code>IncomeFromFactoring</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.13]</code> <code>Income<wbr>From<wbr>Murabahah<wbr>And<wbr>Istishna</code> <i>[E6, G2, I2]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.14]</code> <code>IncomeFromIjarah</code> <i>[C1, G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.15]</code> <code>IncomeFromRevenueSharing</code> <i>[E6, G2, I2]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.16]</code> <code>Income<wbr>From<wbr>Provisions<wbr>And<wbr>Commissions</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.17]</code> <code>AdministrationIncome</code> <i>[G2, G5]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (9):</b><br/><code>+</code> <code>[PL.C.EBT.GP.03]</code> <code>InterestAndFinanceIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.07]</code> <code>IncomeFromConsumerFinancing</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.09]</code> <code>IncomeFromFinanceLease</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.11]</code> <code>IncomeFromOperatingLease</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.12]</code> <code>IncomeFromFactoring</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.13]</code> <code>Income<wbr>From<wbr>Murabahah<wbr>And<wbr>Istishna</code> <i>[E6, G2, I2]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.14]</code> <code>IncomeFromIjarah</code> <i>[C1, G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.17]</code> <code>AdministrationIncome</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.18]</code> <code>IncomeFromGuarantee</code> <i>[G5]</i></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.IS.REV.04]</code> <b><code>securities_brokerage_and_ib_revenue</code></b> &nbsp;<span><i>(Total 8 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Pendapatan Usaha Perusahaan Efek (Brokerage, Underwriting, &amp; Manajer Investasi)</b>: Komisi perantara pedagang efek, jasa penjaminan emisi IPO/obligasi, jasa penasihat keuangan, imbalan manajer investasi, pembiayaan margin, dan administrasi efek.</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan seluruh akun pendapatan operasional pada *entry point* <code>securities</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan aktivitas transaksi pasar modal (komisi broker saham, penjaminan emisi IPO/obligasi, dan biaya kelolaan reksa dana) pada Perusahaan Efek.<br/><b>Saran Analisis:</b> Perhatikan porsi pendapatan berulang (<i>Asset Management Fee</i>) terhadap pendapatan komisi/<i>underwriting</i> yang sangat fluktuatif mengikuti siklus bursa.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G5</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[PL.C.EBT.GP.21]</code> <code>Revenue<wbr>From<wbr>Underwriting<wbr>Activities<wbr>And<wbr>Selling<wbr>Fees</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.23]</code> <code>Revenue<wbr>From<wbr>Investment<wbr>Management<wbr>Services</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_function_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (6):</b><br/><code>+</code> <code>[PL.C.EBT.GP.19]</code> <code>IncomeFromBrokerageActivity</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.20]</code> <code>Income<wbr>From<wbr>Underwriting<wbr>Activities<wbr>And<wbr>Selling<wbr>Fees</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.22]</code> <code>Income<wbr>From<wbr>Investment<wbr>Management<wbr>Services</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.24]</code> <code>Income<wbr>From<wbr>Financial<wbr>Advisory<wbr>Services</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.25]</code> <code>Income<wbr>From<wbr>Financing<wbr>Transactions</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.26]</code> <code>Income<wbr>From<wbr>Securities<wbr>Administration<wbr>Services</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_function_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[PL.C.EBT.GP.19]</code> <code>IncomeFromBrokerageActivity</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.20]</code> <code>Income<wbr>From<wbr>Underwriting<wbr>Activities<wbr>And<wbr>Selling<wbr>Fees</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.IS.REV.05]</code> <b><code>insurance_underwriting_result_net</code></b> &nbsp;<span><i>(Total 25 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Hasil Underwriting Bersih Asuransi (<i>Net Underwriting Income</i>)</b>: Pendapatan premi asuransi bruto, komisi reasuransi, dan ujrah diterima dikurangi premi reasuransi/retrosesi, perubahan cadangan premi (CAPYBMP), beban klaim bersih, perubahan cadangan klaim/manfaat polis masa depan, dan beban komisi/akuisisi polis.</td>
      <td width="34%" valign="top"><b>Net Underwriting Sum</b>: Jumlahkan seluruh pendapatan premi &amp; underwriting (<code>[PL.C.EBT.GP.27-37]</code>) dikurangi seluruh beban klaim &amp; underwriting asuransi (<code>[PL.C.EBT.ON.20-33]</code>).</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan <b>profitabilitas teknis murni bisnis asuransi (<i>underwriting discipline</i>)</b> setelah premi dikurangi klaim, reasuransi, dan komisi agen.<br/><b>Saran Analisis:</b> Asuransi yang sehat wajib mencetak hasil <i>underwriting</i> bersih positif (<b>Combined Ratio &lt; 100%</b>), bukan sekadar menutup rugi klaim dari hasil investasi.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G4</code>, <code>G5</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (13):</b><br/><code>+</code> <code>[PL.C.EBT.GP.27]</code> <code>RevenueFromInsurancePremiums</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.GP.29]</code> <code>ReinsurancePremiums</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.GP.31]</code> <code>Decrease<wbr>Increase<wbr>In<wbr>Unearned<wbr>Premiums</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.GP.32]</code> <code>Decrease<wbr>Increase<wbr>In<wbr>Premium<wbr>Income<wbr>Ceded<wbr>To<wbr>Reinsurancer</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.34]</code> <code>InsuranceCommissionIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.35]</code> <code>UjrahReceived</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.37]</code> <code>OtherInsuranceIncome</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.15]</code> <code>ClaimExpenses</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.16]</code> <code>ReinsuranceClaims</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.18]</code> <code>Increase<wbr>Decrease<wbr>In<wbr>Estimated<wbr>Claims<wbr>Liability</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.24]</code> <code>InsuranceCommissionExpenses</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.25]</code> <code>Acquisition<wbr>Costs<wbr>Of<wbr>Insurance<wbr>Contracts</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.28]</code> <code>OtherInsuranceExpenses</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[PL.C.EBT.GP.27]</code> <code>RevenueFromInsurancePremiums</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.15]</code> <code>ClaimExpenses</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.28]</code> <code>OtherInsuranceExpenses</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G2</code>, <code>G5</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[PL.C.EBT.GP.28]</code> <code>IncomeFromInsurancePremiums</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.34]</code> <code>InsuranceCommissionIncome</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.25]</code> <code>Acquisition<wbr>Costs<wbr>Of<wbr>Insurance<wbr>Contracts</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (8):</b><br/><code>+</code> <code>[PL.C.EBT.GP.28]</code> <code>IncomeFromInsurancePremiums</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.15]</code> <code>ClaimExpenses</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.16]</code> <code>ReinsuranceClaims</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.19]</code> <code>Increase<wbr>Decrease<wbr>In<wbr>Liability<wbr>For<wbr>Future<wbr>Policy<wbr>Benefit</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.20]</code> <code>Increase<wbr>Decrease<wbr>In<wbr>Liabilities<wbr>To<wbr>Policyholder<wbr>In<wbr>Unit<wbr>Linked<wbr>Contracts</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.24]</code> <code>InsuranceCommissionExpenses</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.25]</code> <code>Acquisition<wbr>Costs<wbr>Of<wbr>Insurance<wbr>Contracts</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.27]</code> <code>OtherUnderwritingExpenses</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (20):</b><br/><code>+</code> <code>[PL.C.EBT.GP.27]</code> <code>RevenueFromInsurancePremiums</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.GP.29]</code> <code>ReinsurancePremiums</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.GP.30]</code> <code>RetrocessionPremiums</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.GP.31]</code> <code>Decrease<wbr>Increase<wbr>In<wbr>Unearned<wbr>Premiums</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.GP.32]</code> <code>Decrease<wbr>Increase<wbr>In<wbr>Premium<wbr>Income<wbr>Ceded<wbr>To<wbr>Reinsurancer</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.33]</code> <code>CommissionIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.35]</code> <code>UjrahReceived</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.GP.36]</code> <code>OtherUnderwritingIncome</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.15]</code> <code>ClaimExpenses</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.16]</code> <code>ReinsuranceClaims</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.17]</code> <code>RetrocessionClaims</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.18]</code> <code>Increase<wbr>Decrease<wbr>In<wbr>Estimated<wbr>Claims<wbr>Liability</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.19]</code> <code>Increase<wbr>Decrease<wbr>In<wbr>Liability<wbr>For<wbr>Future<wbr>Policy<wbr>Benefit</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.20]</code> <code>Increase<wbr>Decrease<wbr>In<wbr>Liabilities<wbr>To<wbr>Policyholder<wbr>In<wbr>Unit<wbr>Linked<wbr>Contracts</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.21]</code> <code>Increase<wbr>Decrease<wbr>In<wbr>Provision<wbr>For<wbr>Losses<wbr>Arising<wbr>From<wbr>Liability<wbr>Adequacy<wbr>Test</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.22]</code> <code>Increase<wbr>Decrease<wbr>In<wbr>Insurance<wbr>Liabilities<wbr>Ceded<wbr>To<wbr>Reinsurers</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.23]</code> <code>CommissionExpenses</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.25]</code> <code>Acquisition<wbr>Costs<wbr>Of<wbr>Insurance<wbr>Contracts</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.26]</code> <code>UjrahPaid</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.ON.27]</code> <code>OtherUnderwritingExpenses</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.IS.GP]</code> <b><code>gross_profit_or_net_operating_revenue</code></b> &nbsp;<span><i>(Total 2 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Laba Kotor (Sektor Riil) / Pendapatan Operasional Bersih (Keuangan)</b>: Laba kotor setelah dikurangi HPP pada sektor riil, atau laba operasional sebelum pajak pada sektor keuangan.</td>
      <td width="34%" valign="top"><b>Coalesce / Unified Top-Line Profit</b>: <code>coalesce(GrossProfit, ProfitFromOperation, gross_revenue_real_sector − cost_of_revenue_real_sector)</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan margin keuntungan tingkat pertama dari produk/jasa utama sebelum terbebani biaya overhead manajemen dan beban bunga.<br/><b>Saran Analisis:</b> Jangkar pembanding lintas sektor untuk menghitung <b>Gross Margin</b> (sektor riil) atau <b>Operating Profit</b> (sektor keuangan).</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code>, <code>property</code>, <code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_function_after_tax</code><br/>• <code>by_function_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[PL.C.EBT.GP]</code> <code>GrossProfit</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_nature_after_tax</code><br/>• <code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[PL.C.EBIT]</code> <code>ProfitFromOperation</code></td>
    </tr>
  </tbody>
</table>

### 2.2 Beban Usaha Berdasarkan Fungsi, Sifat, & Pencadangan Kredit (`[CAN.IS.OPEX]`)

<table width="100%">
  <colgroup>
    <col width="34%" />
    <col width="34%" />
    <col width="32%" />
  </colgroup>
  <thead>
    <tr>
      <th align="left" width="34%">Penjelasan / Entry Points / Variant</th>
      <th align="left" width="34%">Aturan Agregasi / Sectors / Accounts</th>
      <th align="left" width="32%">Makna Ekonomi &amp; Saran Analisis / Subsectors</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="3"><code>[CAN.IS.OPEX.01]</code> <b><code>selling_and_general_admin_expenses</code></b> &nbsp;<span><i>(Total 13 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Beban Penjualan, Pemasaran, Umum, Administrasi (SG&amp;A), &amp; Gaji Karyawan</b>: Beban penjualan/distribusi, beban umum &amp; administrasi kantor pusat, gaji dan tunjangan SDM, sewa, pemeliharaan, utilitas, keamanan, interkoneksi, serta beban manajer investasi/kustodian.</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan <code>SellingExpenses + GeneralAndAdministrativeExpenses</code> (varian <i>By Function</i>) serta rincian beban gaji, sewa, utilitas, dan operasional kantor (varian <i>By Nature</i> &amp; sektor keuangan).</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan beban tetap (<i>overhead</i>) untuk menggaji karyawan, memasarkan produk, dan menjalankan administrasi kantor.<br/><b>Saran Analisis:</b> Bandingkan terhadap pendapatan/laba kotor (<b>OPEX-to-Revenue / CIR</b>); kenaikan rasio ini saat omzet stagnan menandakan inefisiensi birokrasi perusahaan.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code>, <code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_function_after_tax</code><br/>• <code>by_function_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>−</code> <code>[PL.C.EBT.OF.01]</code> <code>SellingExpenses</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.OF.02]</code> <code>General<wbr>And<wbr>Administrative<wbr>Expenses</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>C1</code>, <code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code>, <code>J3</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_function_after_tax</code><br/>• <code>by_function_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>−</code> <code>[PL.C.EBT.OF.01]</code> <code>SellingExpenses</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.OF.02]</code> <code>General<wbr>And<wbr>Administrative<wbr>Expenses</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_nature_after_tax</code><br/>• <code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (5):</b><br/><code>+</code> <code>[PL.C.EBT.ON.32]</code> <code>RentalExpenses</code> <i>[E5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.33]</code> <code>Repairs<wbr>And<wbr>Maintenance<wbr>Expenses</code> <i>[E5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.34]</code> <code>UtilityExpenses</code> <i>[E5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.35]</code> <code>SecurityExpenses</code> <i>[E5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.36]</code> <code>HotelExpenses</code> <i>[E5, G5, H1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>C</code>, <code>D</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>C1</code>, <code>D1</code>, <code>D2</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_function_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>−</code> <code>[PL.C.EBT.OF.01]</code> <code>SellingExpenses</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.OF.02]</code> <code>General<wbr>And<wbr>Administrative<wbr>Expenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.37]</code> <code>InterconnectionExpenses</code> <i>[J3, J4, K2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_function_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>−</code> <code>[PL.C.EBT.OF.01]</code> <code>SellingExpenses</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.OF.02]</code> <code>General<wbr>And<wbr>Administrative<wbr>Expenses</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_nature_after_tax</code><br/>• <code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[PL.C.EBT.ON.37]</code> <code>InterconnectionExpenses</code> <i>[J3, J4, K2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_nature_after_tax</code><br/>• <code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>−</code> <code>[PL.C.EBT.OF.01]</code> <code>SellingExpenses</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.OF.02]</code> <code>General<wbr>And<wbr>Administrative<wbr>Expenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.31]</code> <code>Rent<wbr>Maintenance<wbr>And<wbr>Improvement<wbr>Expenses</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.40]</code> <code>Other<wbr>Fees<wbr>And<wbr>Commissions<wbr>Expenses</code> <i>[G1, G5, H1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_nature_after_tax</code><br/>• <code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>−</code> <code>[PL.C.EBT.OF.01]</code> <code>SellingExpenses</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.OF.02]</code> <code>General<wbr>And<wbr>Administrative<wbr>Expenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.29]</code> <code>Salary<wbr>And<wbr>Employee<wbr>Benefit<wbr>Expenses</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>−</code> <code>[PL.C.EBT.OF.02]</code> <code>General<wbr>And<wbr>Administrative<wbr>Expenses</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>collective_investment_contract</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>B</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>B1</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[PL.C.EBT.ON.38]</code> <code>InvestmentManagementExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.39]</code> <code>CustodianExpenses</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.IS.OPEX.02]</code> <b><code>cost_of_production_by_nature_and_da</code></b> &nbsp;<span><i>(Total 15 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Beban Produksi Berdasarkan Sifat (<i>By Nature</i>) &amp; Beban Penyusutan/Amortisasi</b>: Rincian pemakaian bahan baku, barang dagangan, perubahan persediaan barang jadi, biaya kontraktor/pabrikasi, transportasi, pemeliharaan jalan tol, serta beban penyusutan &amp; amortisasi.</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan seluruh akun biaya produksi langsung sifat dan <code>DepreciationAndAmortisationExpenses</code> / <code>DepreciationOfInvestmentPropertyLeaseAssets...</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan rincian struktur biaya produksi berdasarkan sifatnya (bahan baku, kontraktor, energi) sekaligus beban non-kas penyusutan &amp; amortisasi (D&amp;A).<br/><b>Saran Analisis:</b> <b>Kunci perhitungan EBITDA!</b> Ekstrak nilai <code>DepreciationAndAmortisationExpenses</code> dari akun ini untuk ditambahkan kembali ke EBIT.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>B</code>, <code>C</code>, <code>D</code>, <code>E</code>, <code>F</code>, <code>G</code>, <code>I</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>B1</code>, <code>C1</code>, <code>D2</code>, <code>E5</code>, <code>E6</code>, <code>E7</code>, <code>F1</code>, <code>G3</code>, <code>G5</code>, <code>I1</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (13):</b><br/><code>+</code> <code>[PL.C.EBT.ON.01]</code> <code>Program<wbr>And<wbr>Broadcasting<wbr>Expenses</code> <i>[E6]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.03]</code> <code>Increase<wbr>Decrease<wbr>In<wbr>Inventories<wbr>Of<wbr>Finished<wbr>Goods<wbr>And<wbr>Work<wbr>In<wbr>Progress</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.04]</code> <code>EmployeeBenefitsExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.05]</code> <code>HotelOperationExpenses</code> <i>[E5, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.06]</code> <code>NetworkOperationExpenses</code> <i>[C1, I1, J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.07]</code> <code>Ticketing<wbr>Sales<wbr>And<wbr>Promotion<wbr>Expenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.08]</code> <code>Addition<wbr>Reversal<wbr>Of<wbr>Impairment<wbr>Loss<wbr>Recognised<wbr>In<wbr>Profit<wbr>Or<wbr>Loss</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.09]</code> <code>JointOperationsExpenses</code> <i>[B1, G3]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.10]</code> <code>Transportation<wbr>Operation<wbr>Expenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.11]</code> <code>Raw<wbr>Materials<wbr>And<wbr>Consumables<wbr>Used</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.12]</code> <code>ExplorationExpenses</code> <i>[A1]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.13]</code> <code>Depreciation<wbr>And<wbr>Amortisation<wbr>Expenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.14]</code> <code>Maintenance<wbr>And<wbr>Overhaul<wbr>Expenses</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (10):</b><br/><code>+</code> <code>[PL.C.EBT.ON.01]</code> <code>Program<wbr>And<wbr>Broadcasting<wbr>Expenses</code> <i>[E6]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.02]</code> <code>ConstructionExpenses</code> <i>[J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.03]</code> <code>Increase<wbr>Decrease<wbr>In<wbr>Inventories<wbr>Of<wbr>Finished<wbr>Goods<wbr>And<wbr>Work<wbr>In<wbr>Progress</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.04]</code> <code>EmployeeBenefitsExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.05]</code> <code>HotelOperationExpenses</code> <i>[E5, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.07]</code> <code>Ticketing<wbr>Sales<wbr>And<wbr>Promotion<wbr>Expenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.08]</code> <code>Addition<wbr>Reversal<wbr>Of<wbr>Impairment<wbr>Loss<wbr>Recognised<wbr>In<wbr>Profit<wbr>Or<wbr>Loss</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.11]</code> <code>Raw<wbr>Materials<wbr>And<wbr>Consumables<wbr>Used</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.13]</code> <code>Depreciation<wbr>And<wbr>Amortisation<wbr>Expenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.14]</code> <code>Maintenance<wbr>And<wbr>Overhaul<wbr>Expenses</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>E</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>E5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_nature_after_tax</code><br/>• <code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[PL.C.EBT.ON.02]</code> <code>ConstructionExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.04]</code> <code>EmployeeBenefitsExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.08]</code> <code>Addition<wbr>Reversal<wbr>Of<wbr>Impairment<wbr>Loss<wbr>Recognised<wbr>In<wbr>Profit<wbr>Or<wbr>Loss</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.13]</code> <code>Depreciation<wbr>And<wbr>Amortisation<wbr>Expenses</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>J</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>J2</code>, <code>J3</code>, <code>J4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (8):</b><br/><code>+</code> <code>[PL.C.EBT.ON.02]</code> <code>ConstructionExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.04]</code> <code>EmployeeBenefitsExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.06]</code> <code>NetworkOperationExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.07]</code> <code>Ticketing<wbr>Sales<wbr>And<wbr>Promotion<wbr>Expenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.08]</code> <code>Addition<wbr>Reversal<wbr>Of<wbr>Impairment<wbr>Loss<wbr>Recognised<wbr>In<wbr>Profit<wbr>Or<wbr>Loss</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.12]</code> <code>ExplorationExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.13]</code> <code>Depreciation<wbr>And<wbr>Amortisation<wbr>Expenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.14]</code> <code>Maintenance<wbr>And<wbr>Overhaul<wbr>Expenses</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (6):</b><br/><code>+</code> <code>[PL.C.EBT.ON.02]</code> <code>ConstructionExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.04]</code> <code>EmployeeBenefitsExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.07]</code> <code>Ticketing<wbr>Sales<wbr>And<wbr>Promotion<wbr>Expenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.10]</code> <code>Transportation<wbr>Operation<wbr>Expenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.13]</code> <code>Depreciation<wbr>And<wbr>Amortisation<wbr>Expenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.14]</code> <code>Maintenance<wbr>And<wbr>Overhaul<wbr>Expenses</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_nature_after_tax</code><br/>• <code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[PL.C.EBT.ON.30]</code> <code>Depreciation<wbr>Of<wbr>Investment<wbr>Property<wbr>Lease<wbr>Assets<wbr>Property<wbr>And<wbr>Equipment<wbr>Foreclosed<wbr>Assets<wbr>And<wbr>Ijarah<wbr>Assets</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.IS.OPEX.03]</code> <b><code>credit_impairment_provision_net</code></b> &nbsp;<span><i>(Total 13 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Beban Penyisihan Kerugian Penurunan Nilai (CKPN / <i>Provision for Impairment Losses</i>) &amp; Pemulihan Kredit Hapus Buku Bersih</b>: Beban pembentukan cadangan kredit/piutang macet (PSAK 71) atas aset produktif, non-produktif, dan komitmen/kontinjensi dikurangi pemulihan CKPN (<i>recovery</i>) dan penerimaan kembali kredit hapus buku (<i>written-off assets recovery</i>).</td>
      <td width="34%" valign="top"><b>Net Provision (Impairment Expense − Recovery)</b>: Jumlahkan beban pembentukan CKPN dikurangi seluruh akun <code>RecoveryOf...</code> dan <code>RevenueFromRecoveryOfWrittenOffAssets</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan <b>biaya kerusakan kualitas aset/kredit (<i>Cost of Credit</i>)</b> akibat debitur atau pelanggan yang gagal bayar.<br/><b>Saran Analisis:</b> Hitung <b>Cost of Credit (CoC)</b> (<code>credit_impairment_provision_net / loans_and_sharia_financing_net</code>). Lonjakan beban CKPN adalah penyebab utama anjloknya laba bank/multifinance.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (10):</b><br/><code>+</code> <code>[PL.C.EBT.ON.41]</code> <code>Allowances<wbr>For<wbr>Impairment<wbr>Losses<wbr>On<wbr>Earnings<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.42]</code> <code>Allowances<wbr>For<wbr>Impairment<wbr>Losses<wbr>On<wbr>Non<wbr>Earnings<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.43]</code> <code>Reversal<wbr>Expense<wbr>Of<wbr>Estimated<wbr>Losses<wbr>On<wbr>Commitments<wbr>And<wbr>Contingencies</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.46]</code> <code>Recovery<wbr>Of<wbr>Impairment<wbr>Losses<wbr>Of<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.47]</code> <code>Recovery<wbr>Of<wbr>Impairment<wbr>Losses<wbr>Of<wbr>Financial<wbr>Assets<wbr>Consumer<wbr>Financing<wbr>Receivables</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.48]</code> <code>Recovery<wbr>Of<wbr>Impairment<wbr>Losses<wbr>Of<wbr>Financial<wbr>Assets<wbr>Finance<wbr>Lease</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.49]</code> <code>Recovery<wbr>Of<wbr>Impairment<wbr>Losses<wbr>Of<wbr>Nonfinancial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.50]</code> <code>Recovery<wbr>Of<wbr>Impairment<wbr>Losses<wbr>Of<wbr>Nonfinancial<wbr>Assets<wbr>Repossessed<wbr>Collaterals</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.51]</code> <code>Recovery<wbr>Of<wbr>Estimated<wbr>Losses<wbr>Of<wbr>Commitments<wbr>And<wbr>Contingency</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.52]</code> <code>Revenue<wbr>From<wbr>Recovery<wbr>Of<wbr>Written<wbr>Off<wbr>Assets</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (8):</b><br/><code>+</code> <code>[PL.C.EBT.ON.41]</code> <code>Allowances<wbr>For<wbr>Impairment<wbr>Losses<wbr>On<wbr>Earnings<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.42]</code> <code>Allowances<wbr>For<wbr>Impairment<wbr>Losses<wbr>On<wbr>Non<wbr>Earnings<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.43]</code> <code>Reversal<wbr>Expense<wbr>Of<wbr>Estimated<wbr>Losses<wbr>On<wbr>Commitments<wbr>And<wbr>Contingencies</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.46]</code> <code>Recovery<wbr>Of<wbr>Impairment<wbr>Losses<wbr>Of<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.49]</code> <code>Recovery<wbr>Of<wbr>Impairment<wbr>Losses<wbr>Of<wbr>Nonfinancial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.50]</code> <code>Recovery<wbr>Of<wbr>Impairment<wbr>Losses<wbr>Of<wbr>Nonfinancial<wbr>Assets<wbr>Repossessed<wbr>Collaterals</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.51]</code> <code>Recovery<wbr>Of<wbr>Estimated<wbr>Losses<wbr>Of<wbr>Commitments<wbr>And<wbr>Contingency</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.52]</code> <code>Revenue<wbr>From<wbr>Recovery<wbr>Of<wbr>Written<wbr>Off<wbr>Assets</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[PL.C.EBT.ON.44]</code> <code>ProvisionForImpairmentLosses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.45]</code> <code>RecoveryOfImpairmentLosses</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.53]</code> <code>Income<wbr>From<wbr>Recovery<wbr>Of<wbr>Written<wbr>Off<wbr>Assets</code> <i>[G2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[PL.C.EBT.ON.44]</code> <code>ProvisionForImpairmentLosses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.ON.53]</code> <code>Income<wbr>From<wbr>Recovery<wbr>Of<wbr>Written<wbr>Off<wbr>Assets</code> <i>[G2]</i></td>
    </tr>
  </tbody>
</table>

### 2.3 Pendapatan/Beban Keuangan, Bagian Laba Asosiasi, Pajak, & Laba Bersih (`[CAN.IS.EBT]` – `[CAN.IS.NI]`)

<table width="100%">
  <colgroup>
    <col width="34%" />
    <col width="34%" />
    <col width="32%" />
  </colgroup>
  <thead>
    <tr>
      <th align="left" width="34%">Penjelasan / Entry Points / Variant</th>
      <th align="left" width="34%">Aturan Agregasi / Sectors / Accounts</th>
      <th align="left" width="32%">Makna Ekonomi &amp; Saran Analisis / Subsectors</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="3"><code>[CAN.IS.FIN]</code> <b><code>net_finance_and_investment_income</code></b> &nbsp;<span><i>(Total 25 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Pendapatan &amp; Beban Keuangan, Beban Bunga Bank/Multifinance, Hasil Investasi Asuransi/KIK, Trading Efek, &amp; Selisih Kurs</b>: Pendapatan bunga/dividen, hasil investasi asuransi/KIK, keuntungan terealisasi/belum terealisasi perdagangan efek &amp; derivatif, serta selisih kurs dikurangi beban bunga pinjaman/DPK (<code>FinanceCosts</code>, <code>InterestExpenses</code>, <code>RevenueSharingExpenses</code>).</td>
      <td width="34%" valign="top"><b>Sum (Income − Interest/Finance Expense)</b>: Jumlahkan seluruh pendapatan investasi, bunga, trading efek, dan kurs dikurangi <code>FinanceCosts</code>, <code>InterestExpenses</code>, dan <code>RevenueSharingExpenses</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan beban biaya bunga atas utang/simpanan (<i>cost of debt/funds</i>) sekaligus hasil investasi portofolio keuangan dan fluktuasi kurs valas.<br/><b>Saran Analisis:</b> Ekstrak komponen beban bunga (<code>FinanceCosts + InterestExpenses</code>) sebagai penyebut dalam rasio <b>Interest Coverage Ratio (ICR = EBIT / Interest Expense)</b>.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_function_after_tax</code><br/>• <code>by_function_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (11):</b><br/><code>+</code> <code>[PL.C.EBT.FIN.01]</code> <code>InterestAndFinanceCosts</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.02]</code> <code>FinalTaxExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.03]</code> <code>FinanceIncome</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.FIN.04]</code> <code>FinanceCosts</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.05]</code> <code>InterestIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.06]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Foreign<wbr>Exchange<wbr>Rates</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.07]</code> <code>DividendsIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.08]</code> <code>Realised<wbr>Gains<wbr>Losses<wbr>On<wbr>Trading<wbr>Of<wbr>Marketable<wbr>Securities</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.09]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Derivative<wbr>Financial<wbr>Instruments</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.10]</code> <code>InvestmentIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.11]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Marketable<wbr>Securities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (9):</b><br/><code>+</code> <code>[PL.C.EBT.FIN.01]</code> <code>InterestAndFinanceCosts</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.02]</code> <code>FinalTaxExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.03]</code> <code>FinanceIncome</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.FIN.04]</code> <code>FinanceCosts</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.05]</code> <code>InterestIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.07]</code> <code>DividendsIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.08]</code> <code>Realised<wbr>Gains<wbr>Losses<wbr>On<wbr>Trading<wbr>Of<wbr>Marketable<wbr>Securities</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.10]</code> <code>InvestmentIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.11]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Marketable<wbr>Securities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (5):</b><br/><code>+</code> <code>[PL.C.EBT.FIN.01]</code> <code>InterestAndFinanceCosts</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.02]</code> <code>FinalTaxExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.03]</code> <code>FinanceIncome</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.FIN.04]</code> <code>FinanceCosts</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.05]</code> <code>InterestIncome</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>C1</code>, <code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code>, <code>J3</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_function_after_tax</code><br/>• <code>by_function_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[PL.C.EBT.FIN.01]</code> <code>InterestAndFinanceCosts</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.03]</code> <code>FinanceIncome</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.FIN.04]</code> <code>FinanceCosts</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.06]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Foreign<wbr>Exchange<wbr>Rates</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_nature_after_tax</code><br/>• <code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[PL.C.EBT.FIN.01]</code> <code>InterestAndFinanceCosts</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.03]</code> <code>FinanceIncome</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.FIN.04]</code> <code>FinanceCosts</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>C</code>, <code>D</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>C1</code>, <code>D1</code>, <code>D2</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_function_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (5):</b><br/><code>+</code> <code>[PL.C.EBT.FIN.01]</code> <code>InterestAndFinanceCosts</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.03]</code> <code>FinanceIncome</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.FIN.04]</code> <code>FinanceCosts</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.06]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Foreign<wbr>Exchange<wbr>Rates</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.09]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Derivative<wbr>Financial<wbr>Instruments</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_function_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[PL.C.EBT.FIN.01]</code> <code>InterestAndFinanceCosts</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.03]</code> <code>FinanceIncome</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.FIN.04]</code> <code>FinanceCosts</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.06]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Foreign<wbr>Exchange<wbr>Rates</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_nature_after_tax</code><br/>• <code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[PL.C.EBT.FIN.01]</code> <code>InterestAndFinanceCosts</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.03]</code> <code>FinanceIncome</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.FIN.04]</code> <code>FinanceCosts</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (10):</b><br/><code>+</code> <code>[PL.C.EBT.FIN.05]</code> <code>InterestIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.06]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Foreign<wbr>Exchange<wbr>Rates</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.07]</code> <code>DividendsIncome</code> <i>[G1, G5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.08]</code> <code>Realised<wbr>Gains<wbr>Losses<wbr>On<wbr>Trading<wbr>Of<wbr>Marketable<wbr>Securities</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.11]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Marketable<wbr>Securities</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.FIN.12]</code> <code>InterestExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.14]</code> <code>InvestmentsIncome</code> <i>[G1, G4, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.15]</code> <code>NetInvestmentIncome</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.16]</code> <code>Revenue<wbr>From<wbr>Trading<wbr>Transactions</code> <i>[G1, G5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.24]</code> <code>Realised<wbr>Gains<wbr>Losses<wbr>From<wbr>Derivative<wbr>Instruments</code> <i>[G1, G5, H1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (9):</b><br/><code>+</code> <code>[PL.C.EBT.FIN.05]</code> <code>InterestIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.06]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Foreign<wbr>Exchange<wbr>Rates</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.07]</code> <code>DividendsIncome</code> <i>[G1, G5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.08]</code> <code>Realised<wbr>Gains<wbr>Losses<wbr>On<wbr>Trading<wbr>Of<wbr>Marketable<wbr>Securities</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.11]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Marketable<wbr>Securities</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.FIN.12]</code> <code>InterestExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.14]</code> <code>InvestmentsIncome</code> <i>[G1, G4, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.16]</code> <code>Revenue<wbr>From<wbr>Trading<wbr>Transactions</code> <i>[G1, G5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.24]</code> <code>Realised<wbr>Gains<wbr>Losses<wbr>From<wbr>Derivative<wbr>Instruments</code> <i>[G1, G5, H1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (6):</b><br/><code>+</code> <code>[PL.C.EBT.FIN.01]</code> <code>InterestAndFinanceCosts</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.FIN.04]</code> <code>FinanceCosts</code> <i>[C1, G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.06]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Foreign<wbr>Exchange<wbr>Rates</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.FIN.12]</code> <code>InterestExpenses</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.FIN.13]</code> <code>RevenueSharingExpenses</code> <i>[C1, G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.19]</code> <code>Unrealised<wbr>Gains<wbr>Losses<wbr>On<wbr>Trading<wbr>Of<wbr>Financial<wbr>Assets</code> <i>[G2, G5]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (6):</b><br/><code>+</code> <code>[PL.C.EBT.FIN.01]</code> <code>InterestAndFinanceCosts</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.06]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Foreign<wbr>Exchange<wbr>Rates</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.FIN.12]</code> <code>InterestExpenses</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.FIN.13]</code> <code>RevenueSharingExpenses</code> <i>[C1, G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.18]</code> <code>Realised<wbr>Gains<wbr>Losses<wbr>On<wbr>Trading<wbr>Of<wbr>Financial<wbr>Assets</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.19]</code> <code>Unrealised<wbr>Gains<wbr>Losses<wbr>On<wbr>Trading<wbr>Of<wbr>Financial<wbr>Assets</code> <i>[G2, G5]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (6):</b><br/><code>+</code> <code>[PL.C.EBT.FIN.01]</code> <code>InterestAndFinanceCosts</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.15]</code> <code>NetInvestmentIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.20]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Sale<wbr>Of<wbr>Shares<wbr>Of<wbr>Stock</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.21]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Sale<wbr>Of<wbr>Available<wbr>For<wbr>Sale<wbr>Securities</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.22]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Sale<wbr>Of<wbr>Securities<wbr>And<wbr>Mutual<wbr>Funds<wbr>At<wbr>Fair<wbr>Value<wbr>Through<wbr>Profit<wbr>Or<wbr>Loss</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.23]</code> <code>Unrealised<wbr>Fair<wbr>Value<wbr>Gains<wbr>Losses<wbr>On<wbr>Securities<wbr>And<wbr>Mutual<wbr>Funds<wbr>At<wbr>Fair<wbr>Value<wbr>Through<wbr>Profit<wbr>Or<wbr>Loss</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_function_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (7):</b><br/><code>+</code> <code>[PL.C.EBT.FIN.02]</code> <code>FinalTaxExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.03]</code> <code>FinanceIncome</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.FIN.04]</code> <code>FinanceCosts</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.07]</code> <code>DividendsIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.08]</code> <code>Realised<wbr>Gains<wbr>Losses<wbr>On<wbr>Trading<wbr>Of<wbr>Marketable<wbr>Securities</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.11]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Marketable<wbr>Securities</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.25]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Foreign<wbr>Exchange<wbr>Transactions</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_function_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (6):</b><br/><code>+</code> <code>[PL.C.EBT.FIN.02]</code> <code>FinalTaxExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.03]</code> <code>FinanceIncome</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.FIN.04]</code> <code>FinanceCosts</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.07]</code> <code>DividendsIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.08]</code> <code>Realised<wbr>Gains<wbr>Losses<wbr>On<wbr>Trading<wbr>Of<wbr>Marketable<wbr>Securities</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.11]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Marketable<wbr>Securities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>collective_investment_contract</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>B</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>B1</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[PL.C.EBT.FIN.05]</code> <code>InterestIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.07]</code> <code>DividendsIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.FIN.17]</code> <code>Gains<wbr>Losses<wbr>From<wbr>Securities<wbr>Portfolio</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.IS.EQ]</code> <b><code>share_of_profit_loss_associates_and_jv</code></b> &nbsp;<span><i>(Total 2 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Bagian Laba (Rugi) Bersih dari Entitas Asosiasi &amp; Ventura Bersama (Metode Ekuitas)</b>: Porsi laba/rugi bersih dari perusahaan asosiasi (kepemilikan 20%–50%) dan <i>joint venture</i>.</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan seluruh akun <code>[PL.C.EBT.EQ.01-03]</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan kontribusi laba/rugi dari perusahaan patungan (<i>Joint Venture</i>) dan entitas asosiasi (kepemilikan 20%–50%).<br/><b>Saran Analisis:</b> Ingat bahwa ini adalah <b>laba akuntansi non-kas</b>; cek penerimaan dividen tunai di Arus Kas Investasi (<code>[CAN.CF.CFI.03]</code>) untuk memastikan labanya benar-benar menyetor kas.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code>, <code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>B1</code>, <code>C1</code>, <code>C2</code>, <code>C3</code>, <code>D1</code>, <code>D2</code>, <code>D3</code>, <code>D4</code>, <code>E1</code>, <code>E2</code>, <code>E4</code>, <code>E5</code>, <code>E6</code>, <code>E7</code>, <code>F1</code>, <code>F2</code>, <code>G5</code>, <code>H1</code>, <code>I1</code>, <code>I2</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_function_after_tax</code><br/>• <code>by_function_before_tax</code><br/>• <code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[PL.C.EBT.EQ.01]</code> <code>Share<wbr>Of<wbr>Profit<wbr>Loss<wbr>Of<wbr>Joint<wbr>Ventures<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.EQ.02]</code> <code>Share<wbr>Of<wbr>Profit<wbr>Loss<wbr>Of<wbr>Associates<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_function_after_tax</code><br/>• <code>by_function_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[PL.C.EBT.EQ.01]</code> <code>Share<wbr>Of<wbr>Profit<wbr>Loss<wbr>Of<wbr>Joint<wbr>Ventures<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.EQ.02]</code> <code>Share<wbr>Of<wbr>Profit<wbr>Loss<wbr>Of<wbr>Associates<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[PL.C.EBT.EQ.02]</code> <code>Share<wbr>Of<wbr>Profit<wbr>Loss<wbr>Of<wbr>Associates<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code>, <code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>E6</code>, <code>G1</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_nature_after_tax</code><br/>• <code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[PL.C.EBT.EQ.02]</code> <code>Share<wbr>Of<wbr>Profit<wbr>Loss<wbr>Of<wbr>Associates<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.IS.OTH]</code> <b><code>other_non_operating_gains_losses</code></b> &nbsp;<span><i>(Total 11 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Keuntungan (Kerugian) Non-Operasional &amp; Pos Satu Kali (<i>One-Off Items</i>)</b>: Keuntungan/kerugian pelepasan aset tetap/AYDA, perubahan nilai wajar properti investasi, pendapatan/beban operasional &amp; non-operasional lainnya, dan pajak final.</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan seluruh akun <code>[PL.C.EBT.OTH.01-11]</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan keuntungan atau kerugian insidental di luar bisnis utama (seperti jual aset tetap, klaim asuransi, atau penyesuaian nilai wajar satu kali).<br/><b>Saran Analisis:</b> <b>Keluarkan akun ini saat menghitung Core Profit (Laba Inti)!</b> Emiten yang laba bersihnya tinggi hanya karena <code>OtherGainsLosses</code> memiliki kualitas laba yang rendah.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code>, <code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b> <code>all_variants</code><br/>• <code>by_function_after_tax</code><br/>• <code>by_function_before_tax</code><br/>• <code>by_nature_after_tax</code><br/>• <code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[PL.C.EBT.OTH.01]</code> <code>OtherGainsLosses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.OTH.02]</code> <code>OtherIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.OTH.03]</code> <code>OtherExpenses</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>C</code>, <code>D</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>C1</code>, <code>D1</code>, <code>D2</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_function_after_tax</code><br/>• <code>by_function_before_tax</code><br/>• <code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[PL.C.EBT.OTH.01]</code> <code>OtherGainsLosses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.OTH.02]</code> <code>OtherIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.OTH.03]</code> <code>OtherExpenses</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[PL.C.EBT.OTH.01]</code> <code>OtherGainsLosses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.OTH.03]</code> <code>OtherExpenses</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_nature_after_tax</code><br/>• <code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (6):</b><br/><code>+</code> <code>[PL.C.EBT.OTH.04]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Disposal<wbr>Of<wbr>Property<wbr>And<wbr>Equipment</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.OTH.05]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Disposal<wbr>Of<wbr>Foreclosed<wbr>Assets</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.OTH.06]</code> <code>OtherOperatingIncome</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.OTH.07]</code> <code>OtherOperatingExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.OTH.08]</code> <code>NonOperatingIncome</code> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.OTH.09]</code> <code>NonOperatingExpenses</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (5):</b><br/><code>+</code> <code>[PL.C.EBT.OTH.02]</code> <code>OtherIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.OTH.03]</code> <code>OtherExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.OTH.04]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Disposal<wbr>Of<wbr>Property<wbr>And<wbr>Equipment</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.OTH.10]</code> <code>OtherGains</code> <i>[G2]</i> &nbsp;·&nbsp; <code>−</code> <code>[PL.C.EBT.OTH.11]</code> <code>OtherLosses</code> <i>[G2, G5]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[PL.C.EBT.OTH.02]</code> <code>OtherIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.OTH.03]</code> <code>OtherExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.OTH.04]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Disposal<wbr>Of<wbr>Property<wbr>And<wbr>Equipment</code> <i>[G2, G5]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_function_after_tax</code><br/>• <code>by_function_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[PL.C.EBT.OTH.01]</code> <code>OtherGainsLosses</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.OTH.02]</code> <code>OtherIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.C.EBT.OTH.03]</code> <code>OtherExpenses</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>collective_investment_contract</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>B</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>B1</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[PL.C.EBT.OTH.03]</code> <code>OtherExpenses</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.IS.EBT]</code> <b><code>profit_loss_before_tax</code></b> &nbsp;<span><i>(Total 1 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Laba (Rugi) Sebelum Pajak Penghasilan (<i>Earnings Before Tax / EBT</i>)</b>: Keuntungan perusahaan setelah seluruh pendapatan dan beban operasional maupun non-operasional diperhitungkan, sebelum dipotong PPh Badan.</td>
      <td width="34%" valign="top"><b>Direct Anchor</b>: Ambil langsung dari <code>[PL.C.EBT] ProfitLossBeforeIncomeTax</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan kemampuan total perusahaan mencetak keuntungan setelah seluruh biaya operasional dan beban bunga utang terpenuhi, sebelum dipotong pajak.<br/><b>Saran Analisis:</b> Metrik terbaik untuk membandingkan daya menghasilkan laba murni antar-perusahaan sebelum distorsi tarif pajak efektif.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code>, <code>property</code>, <code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b> <code>all_variants</code><br/>• <code>by_function_after_tax</code><br/>• <code>by_function_before_tax</code><br/>• <code>by_nature_after_tax</code><br/>• <code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[PL.C.EBT]</code> <code>ProfitLossBeforeIncomeTax</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code>, <code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_nature_after_tax</code><br/>• <code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[PL.C.EBT]</code> <code>ProfitLossBeforeIncomeTax</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[PL.C.EBT]</code> <code>ProfitLossBeforeIncomeTax</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_function_after_tax</code><br/>• <code>by_function_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[PL.C.EBT]</code> <code>ProfitLossBeforeIncomeTax</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>collective_investment_contract</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>B</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>B1</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[PL.C.EBT]</code> <code>ProfitLossBeforeIncomeTax</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.IS.TAX]</code> <b><code>income_tax_expense_benefit</code></b> &nbsp;<span><i>(Total 1 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Beban (Manfaat) Pajak Penghasilan Badan</b>: Total pajak penghasilan kini dan pajak tangguhan atas laba periode berjalan.</td>
      <td width="34%" valign="top"><b>Direct</b>: Ambil dari <code>[PL.C.TAX] TaxBenefitExpenses</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan beban kewajiban pajak penghasilan korporasi kepada negara atas laba yang diperoleh.<br/><b>Saran Analisis:</b> Hitung <b>Effective Tax Rate</b> (<code>income_tax_expense_benefit / profit_loss_before_tax</code>); deviasi jauh dari tarif PPh Badan 22% menandakan adanya pajak final atau kompensasi rugi fiskal.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code>, <code>property</code>, <code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b> <code>all_variants</code><br/>• <code>by_function_after_tax</code><br/>• <code>by_function_before_tax</code><br/>• <code>by_nature_after_tax</code><br/>• <code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[PL.C.TAX]</code> <code>TaxBenefitExpenses</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code>, <code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_nature_after_tax</code><br/>• <code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[PL.C.TAX]</code> <code>TaxBenefitExpenses</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[PL.C.TAX]</code> <code>TaxBenefitExpenses</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_function_after_tax</code><br/>• <code>by_function_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[PL.C.TAX]</code> <code>TaxBenefitExpenses</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.IS.CONT]</code> <b><code>profit_loss_continuing_and_discontinued</code></b> &nbsp;<span><i>(Total 2 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Laba (Rugi) dari Operasi yang Dilanjutkan &amp; Operasi yang Dihentikan</b>: Pemisahan antara laba bersih dari bisnis aktif yang terus berjalan vs laba/rugi dari divisi/anak usaha yang telah ditutup atau dijual.</td>
      <td width="34%" valign="top"><b>Direct</b>: <code>ProfitLossFromContinuingOperations</code> (bisnis aktif) dan <code>ProfitLossFromDiscontinuedOperations</code> (bisnis dihentikan).</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan pemisahan antara kinerja bisnis yang masih terus beroperasi aktif vs dampak pelepasan/penutupan unit bisnis yang dihentikan.<br/><b>Saran Analisis:</b> Gunakan selalu <code>ProfitLossFromContinuingOperations</code> sebagai dasar proyeksi kinerja masa depan.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_function_after_tax</code><br/>• <code>by_function_before_tax</code><br/>• <code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[PL.C]</code> <code>Profit<wbr>Loss<wbr>From<wbr>Continuing<wbr>Operations</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.D]</code> <code>Profit<wbr>Loss<wbr>From<wbr>Discontinued<wbr>Operations</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[PL.C]</code> <code>Profit<wbr>Loss<wbr>From<wbr>Continuing<wbr>Operations</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code>, <code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>A</code>, <code>C</code>, <code>D</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>A1</code>, <code>C1</code>, <code>D1</code>, <code>D2</code>, <code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_function_after_tax</code><br/>• <code>by_function_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[PL.C]</code> <code>Profit<wbr>Loss<wbr>From<wbr>Continuing<wbr>Operations</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.D]</code> <code>Profit<wbr>Loss<wbr>From<wbr>Discontinued<wbr>Operations</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_nature_after_tax</code><br/>• <code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[PL.C]</code> <code>Profit<wbr>Loss<wbr>From<wbr>Continuing<wbr>Operations</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[PL.C]</code> <code>Profit<wbr>Loss<wbr>From<wbr>Continuing<wbr>Operations</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.D]</code> <code>Profit<wbr>Loss<wbr>From<wbr>Discontinued<wbr>Operations</code> <i>[G1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[PL.C]</code> <code>Profit<wbr>Loss<wbr>From<wbr>Continuing<wbr>Operations</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_nature_after_tax</code><br/>• <code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[PL.C]</code> <code>Profit<wbr>Loss<wbr>From<wbr>Continuing<wbr>Operations</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[PL.C]</code> <code>Profit<wbr>Loss<wbr>From<wbr>Continuing<wbr>Operations</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.D]</code> <code>Profit<wbr>Loss<wbr>From<wbr>Discontinued<wbr>Operations</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_function_after_tax</code><br/>• <code>by_function_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[PL.C]</code> <code>Profit<wbr>Loss<wbr>From<wbr>Continuing<wbr>Operations</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.IS.NI]</code> <b><code>net_income_consolidated</code></b> &nbsp;<span><i>(Total 1 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Laba (Rugi) Bersih Konsolidasi Periode Berjalan</b>: Total laba bersih setelah pajak dari seluruh operasi sebelum dipisahkan antara pemilik induk dan minoritas.</td>
      <td width="34%" valign="top"><b>Direct Anchor</b>: Ambil langsung dari <code>[PL] ProfitLoss</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan hasil akhir keuntungan/kerugian bersih seluruh grup usaha konsolidasi pada periode berjalan.<br/><b>Saran Analisis:</b> Menjadi angka jangkar awal pada rekonsiliasi Arus Kas Operasi Metode Tidak Langsung dan pembanding utama terhadap <code>operating_cash_flow</code>.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code>, <code>property</code>, <code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b> <code>all_variants</code><br/>• <code>by_function_after_tax</code><br/>• <code>by_function_before_tax</code><br/>• <code>by_nature_after_tax</code><br/>• <code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[PL]</code> <code>ProfitLoss</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code>, <code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_nature_after_tax</code><br/>• <code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[PL]</code> <code>ProfitLoss</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[PL]</code> <code>ProfitLoss</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_function_after_tax</code><br/>• <code>by_function_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[PL]</code> <code>ProfitLoss</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>collective_investment_contract</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>B</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>B1</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[PL]</code> <code>ProfitLoss</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.IS.NI.P]</code> <b><code>net_income_attributable_to_parent</code></b> &nbsp;<span><i>(Total 2 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Laba (Rugi) Bersih yang Dapat Diatribusikan ke Pemilik Entitas Induk &amp; Nonpengendali</b>: Laba bersih murni yang menjadi hak pemegang saham emiten induk (<code>[PL.P]</code>) vs bagian minoritas anak usaha (<code>[PL.NCI]</code>).</td>
      <td width="34%" valign="top"><b>Coalesce Priority</b>: <code>coalesce(ProfitLossAttributableToParentEntity, ProfitLoss − ProfitLossAttributableToNonControllingInterests, ProfitLoss)</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan <b>hak laba bersih murni milik pemegang saham emiten induk</b> setelah dikurangi bagian laba milik mitra minoritas di anak usaha.<br/><b>Saran Analisis:</b> <b>Angka Laba Bersih (Bottom Line) utama!</b> Wajib digunakan sebagai pembilang untuk menghitung <b>ROE</b>, <b>ROA</b>, <b>Net Profit Margin (NPM)</b>, dan <b>EPS</b>.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code>, <code>property</code>, <code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b> <code>all_variants</code><br/>• <code>by_function_after_tax</code><br/>• <code>by_function_before_tax</code><br/>• <code>by_nature_after_tax</code><br/>• <code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[PL.P]</code> <code>Profit<wbr>Loss<wbr>Attributable<wbr>To<wbr>Parent<wbr>Entity</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.NCI]</code> <code>Profit<wbr>Loss<wbr>Attributable<wbr>To<wbr>Non<wbr>Controlling<wbr>Interests</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code>, <code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_nature_after_tax</code><br/>• <code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[PL.P]</code> <code>Profit<wbr>Loss<wbr>Attributable<wbr>To<wbr>Parent<wbr>Entity</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.NCI]</code> <code>Profit<wbr>Loss<wbr>Attributable<wbr>To<wbr>Non<wbr>Controlling<wbr>Interests</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[PL.P]</code> <code>Profit<wbr>Loss<wbr>Attributable<wbr>To<wbr>Parent<wbr>Entity</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.NCI]</code> <code>Profit<wbr>Loss<wbr>Attributable<wbr>To<wbr>Non<wbr>Controlling<wbr>Interests</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_function_after_tax</code><br/>• <code>by_function_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[PL.P]</code> <code>Profit<wbr>Loss<wbr>Attributable<wbr>To<wbr>Parent<wbr>Entity</code> &nbsp;·&nbsp; <code>+</code> <code>[PL.NCI]</code> <code>Profit<wbr>Loss<wbr>Attributable<wbr>To<wbr>Non<wbr>Controlling<wbr>Interests</code></td>
    </tr>
  </tbody>
</table>

### 2.4 Penghasilan Komprehensif Lain (`[CAN.IS.OCI]`), Total Komprehensif (`[CAN.IS.CI]`), & EPS (`[CAN.IS.EPS]`)

<table width="100%">
  <colgroup>
    <col width="34%" />
    <col width="34%" />
    <col width="32%" />
  </colgroup>
  <thead>
    <tr>
      <th align="left" width="34%">Penjelasan / Entry Points / Variant</th>
      <th align="left" width="34%">Aturan Agregasi / Sectors / Accounts</th>
      <th align="left" width="32%">Makna Ekonomi &amp; Saran Analisis / Subsectors</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="3"><code>[CAN.IS.OCI]</code> <b><code>other_comprehensive_income_after_tax</code></b> &nbsp;<span><i>(Total 41 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Total Penghasilan Komprehensif Lain Setelah Pajak (OCI)</b>: Keuntungan/kerugian belum terealisasi dari revaluasi aset tetap, pengukuran kembali aktuaria pensiun, selisih kurs penjabaran laporan keuangan, lindung nilai arus kas, dan perubahan nilai wajar efek FVOCI (baik varian sebelum maupun setelah pajak).</td>
      <td width="34%" valign="top"><b>Priority / Sum</b>: Ambil langsung dari <code>[OCI] OtherComprehensiveIncomeAfterTax</code>, atau <code>OtherComprehensiveIncomeBeforeTax − TaxOnOtherComprehensiveIncome</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan keuntungan/kerugian belum terealisasi (selisih kurs translasi, perubahan nilai wajar obligasi FVOCI, revaluasi aset, aktuaria pensiun) yang langsung mengubah Ekuitas tanpa lewat Laba Bersih.<br/><b>Saran Analisis:</b> Pada perbankan dan asuransi, OCI negatif besar saat suku bunga naik menggambarkan penurunan nilai pasar portofolio obligasi (<i>unrealized bond losses</i>).</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_function_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (19):</b><br/><code>+</code> <code>[OCI]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.01]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Gains<wbr>Losses<wbr>On<wbr>Revaluation<wbr>Of<wbr>Property<wbr>Plant<wbr>And<wbr>Equipment<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.02]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Remeasurement<wbr>Of<wbr>Defined<wbr>Benefit<wbr>Obligation<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.03]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.01]</code> <code>Share<wbr>Of<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Of<wbr>Associates<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.02]</code> <code>Unrealised<wbr>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.03]</code> <code>Unrealised<wbr>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Financial<wbr>Assets<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.04]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.05]</code> <code>Reclassification<wbr>Adjustments<wbr>On<wbr>Cash<wbr>Flow<wbr>Hedges<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.06]</code> <code>Share<wbr>Of<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Of<wbr>Joint<wbr>Ventures<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.07]</code> <code>Reclassification<wbr>Adjustments<wbr>On<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Financial<wbr>Assets<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.08]</code> <code>Reclassification<wbr>Adjustments<wbr>On<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.09]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Hedges<wbr>Of<wbr>Net<wbr>Investments<wbr>In<wbr>Foreign<wbr>Operations<wbr>After<wbr>Tax</code> <i>[A1, B1, D2]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.10]</code> <code>Reclassification<wbr>Adjustments<wbr>On<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.11]</code> <code>Carrying<wbr>Amount<wbr>Of<wbr>Non<wbr>Financial<wbr>Asset<wbr>Liability<wbr>Whose<wbr>Acquisition<wbr>Or<wbr>Incurrence<wbr>Was<wbr>Hedged<wbr>On<wbr>Highly<wbr>Probable<wbr>Forecast<wbr>Transaction<wbr>Adjusted<wbr>From<wbr>Equity<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.12]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.13]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Cash<wbr>Flow<wbr>Hedges<wbr>After<wbr>Tax</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_function_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (21):</b><br/><code>+</code> <code>[OCI]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.BT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.TAX]</code> <code>Tax<wbr>On<wbr>Other<wbr>Comprehensive<wbr>Income</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT.01]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Remeasurement<wbr>Of<wbr>Defined<wbr>Benefit<wbr>Obligation<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT.02]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT.03]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Gains<wbr>Losses<wbr>On<wbr>Revaluation<wbr>Of<wbr>Property<wbr>Plant<wbr>And<wbr>Equipment<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.01]</code> <code>Unrealised<wbr>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Financial<wbr>Assets<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.02]</code> <code>Carrying<wbr>Amount<wbr>Of<wbr>Non<wbr>Financial<wbr>Asset<wbr>Liability<wbr>Whose<wbr>Acquisition<wbr>Or<wbr>Incurrence<wbr>Was<wbr>Hedged<wbr>On<wbr>Highly<wbr>Probable<wbr>Forecast<wbr>Transaction<wbr>Adjusted<wbr>From<wbr>Equity<wbr>Before<wbr>Tax</code> <i>[I1]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.03]</code> <code>Reclassification<wbr>Adjustments<wbr>On<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Financial<wbr>Assets<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.04]</code> <code>Unrealised<wbr>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.05]</code> <code>Share<wbr>Of<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Of<wbr>Joint<wbr>Ventures<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method<wbr>Before<wbr>Tax</code> <i>[A1, C3, D2]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.06]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Hedges<wbr>Of<wbr>Net<wbr>Investments<wbr>In<wbr>Foreign<wbr>Operations<wbr>Before<wbr>Tax</code> <i>[E7]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.07]</code> <code>Share<wbr>Of<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Of<wbr>Associates<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.08]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.09]</code> <code>Reclassification<wbr>Adjustments<wbr>On<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.10]</code> <code>Reclassification<wbr>Adjustments<wbr>On<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets<wbr>Before<wbr>Tax</code> <i>[B1]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.11]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Cash<wbr>Flow<wbr>Hedges<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.12]</code> <code>Reclassification<wbr>Adjustments<wbr>On<wbr>Cash<wbr>Flow<wbr>Hedges<wbr>Before<wbr>Tax</code> <i>[E5]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.13]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation<wbr>Before<wbr>Tax</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (13):</b><br/><code>+</code> <code>[OCI]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.01]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Gains<wbr>Losses<wbr>On<wbr>Revaluation<wbr>Of<wbr>Property<wbr>Plant<wbr>And<wbr>Equipment<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.02]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Remeasurement<wbr>Of<wbr>Defined<wbr>Benefit<wbr>Obligation<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.03]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.01]</code> <code>Share<wbr>Of<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Of<wbr>Associates<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.03]</code> <code>Unrealised<wbr>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Financial<wbr>Assets<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.04]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.07]</code> <code>Reclassification<wbr>Adjustments<wbr>On<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Financial<wbr>Assets<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.09]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Hedges<wbr>Of<wbr>Net<wbr>Investments<wbr>In<wbr>Foreign<wbr>Operations<wbr>After<wbr>Tax</code> <i>[A1, B1, D2]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.12]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.13]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Cash<wbr>Flow<wbr>Hedges<wbr>After<wbr>Tax</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (12):</b><br/><code>+</code> <code>[OCI]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.BT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.TAX]</code> <code>Tax<wbr>On<wbr>Other<wbr>Comprehensive<wbr>Income</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT.01]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Remeasurement<wbr>Of<wbr>Defined<wbr>Benefit<wbr>Obligation<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT.02]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT.03]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Gains<wbr>Losses<wbr>On<wbr>Revaluation<wbr>Of<wbr>Property<wbr>Plant<wbr>And<wbr>Equipment<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.01]</code> <code>Unrealised<wbr>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Financial<wbr>Assets<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.04]</code> <code>Unrealised<wbr>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.09]</code> <code>Reclassification<wbr>Adjustments<wbr>On<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.13]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation<wbr>Before<wbr>Tax</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>C1</code>, <code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code>, <code>J3</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_function_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (13):</b><br/><code>+</code> <code>[OCI]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.02]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Remeasurement<wbr>Of<wbr>Defined<wbr>Benefit<wbr>Obligation<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.03]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.04]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Gains<wbr>Losses<wbr>On<wbr>Revaluation<wbr>Of<wbr>Property<wbr>And<wbr>Equipment<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.01]</code> <code>Share<wbr>Of<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Of<wbr>Associates<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method<wbr>After<wbr>Tax</code> <i>[E5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.02]</code> <code>Unrealised<wbr>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets<wbr>After<wbr>Tax</code> <i>[E5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.04]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.05]</code> <code>Reclassification<wbr>Adjustments<wbr>On<wbr>Cash<wbr>Flow<wbr>Hedges<wbr>After<wbr>Tax</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.10]</code> <code>Reclassification<wbr>Adjustments<wbr>On<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets<wbr>After<wbr>Tax</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.12]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.13]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Cash<wbr>Flow<wbr>Hedges<wbr>After<wbr>Tax</code> <i>[H1, K1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_function_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (14):</b><br/><code>+</code> <code>[OCI]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.BT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.TAX]</code> <code>Tax<wbr>On<wbr>Other<wbr>Comprehensive<wbr>Income</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT.01]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Remeasurement<wbr>Of<wbr>Defined<wbr>Benefit<wbr>Obligation<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT.02]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT.04]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Gains<wbr>Losses<wbr>On<wbr>Revaluation<wbr>Of<wbr>Property<wbr>And<wbr>Equipment<wbr>Before<wbr>Tax</code> <i>[E5, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.04]</code> <code>Unrealised<wbr>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets<wbr>Before<wbr>Tax</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.07]</code> <code>Share<wbr>Of<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Of<wbr>Associates<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method<wbr>Before<wbr>Tax</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.08]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> <i>[H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.10]</code> <code>Reclassification<wbr>Adjustments<wbr>On<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets<wbr>Before<wbr>Tax</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.11]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Cash<wbr>Flow<wbr>Hedges<wbr>Before<wbr>Tax</code> <i>[J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.13]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation<wbr>Before<wbr>Tax</code> <i>[E5, H1, J2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (7):</b><br/><code>+</code> <code>[OCI]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.02]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Remeasurement<wbr>Of<wbr>Defined<wbr>Benefit<wbr>Obligation<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.03]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.04]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.12]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (8):</b><br/><code>+</code> <code>[OCI]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.BT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.TAX]</code> <code>Tax<wbr>On<wbr>Other<wbr>Comprehensive<wbr>Income</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT.01]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Remeasurement<wbr>Of<wbr>Defined<wbr>Benefit<wbr>Obligation<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT.02]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.13]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation<wbr>Before<wbr>Tax</code> <i>[E5, H1, J2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>C</code>, <code>D</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>C1</code>, <code>D1</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_function_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (16):</b><br/><code>+</code> <code>[OCI]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.02]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Remeasurement<wbr>Of<wbr>Defined<wbr>Benefit<wbr>Obligation<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.03]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.04]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Gains<wbr>Losses<wbr>On<wbr>Revaluation<wbr>Of<wbr>Property<wbr>And<wbr>Equipment<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.01]</code> <code>Share<wbr>Of<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Of<wbr>Associates<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.02]</code> <code>Unrealised<wbr>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.04]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.05]</code> <code>Reclassification<wbr>Adjustments<wbr>On<wbr>Cash<wbr>Flow<wbr>Hedges<wbr>After<wbr>Tax</code> <i>[A1, J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.06]</code> <code>Share<wbr>Of<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Of<wbr>Joint<wbr>Ventures<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method<wbr>After<wbr>Tax</code> <i>[J2, J3, K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.08]</code> <code>Reclassification<wbr>Adjustments<wbr>On<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation<wbr>After<wbr>Tax</code> <i>[A1, J2, J4]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.09]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Hedges<wbr>Of<wbr>Net<wbr>Investments<wbr>In<wbr>Foreign<wbr>Operations<wbr>After<wbr>Tax</code> <i>[J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.10]</code> <code>Reclassification<wbr>Adjustments<wbr>On<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets<wbr>After<wbr>Tax</code> <i>[A1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.12]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.13]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Cash<wbr>Flow<wbr>Hedges<wbr>After<wbr>Tax</code> <i>[J1, J3, K1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_function_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (15):</b><br/><code>+</code> <code>[OCI]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.BT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.TAX]</code> <code>Tax<wbr>On<wbr>Other<wbr>Comprehensive<wbr>Income</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT.01]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Remeasurement<wbr>Of<wbr>Defined<wbr>Benefit<wbr>Obligation<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT.02]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT.04]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Gains<wbr>Losses<wbr>On<wbr>Revaluation<wbr>Of<wbr>Property<wbr>And<wbr>Equipment<wbr>Before<wbr>Tax</code> <i>[J2, J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.02]</code> <code>Carrying<wbr>Amount<wbr>Of<wbr>Non<wbr>Financial<wbr>Asset<wbr>Liability<wbr>Whose<wbr>Acquisition<wbr>Or<wbr>Incurrence<wbr>Was<wbr>Hedged<wbr>On<wbr>Highly<wbr>Probable<wbr>Forecast<wbr>Transaction<wbr>Adjusted<wbr>From<wbr>Equity<wbr>Before<wbr>Tax</code> <i>[K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.04]</code> <code>Unrealised<wbr>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets<wbr>Before<wbr>Tax</code> <i>[J3, K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.07]</code> <code>Share<wbr>Of<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Of<wbr>Associates<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method<wbr>Before<wbr>Tax</code> <i>[J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.08]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> <i>[J3, K1, K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.11]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Cash<wbr>Flow<wbr>Hedges<wbr>Before<wbr>Tax</code> <i>[J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.12]</code> <code>Reclassification<wbr>Adjustments<wbr>On<wbr>Cash<wbr>Flow<wbr>Hedges<wbr>Before<wbr>Tax</code> <i>[J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.13]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation<wbr>Before<wbr>Tax</code> <i>[J3, J4, K2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (11):</b><br/><code>+</code> <code>[OCI]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.02]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Remeasurement<wbr>Of<wbr>Defined<wbr>Benefit<wbr>Obligation<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.03]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.04]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Gains<wbr>Losses<wbr>On<wbr>Revaluation<wbr>Of<wbr>Property<wbr>And<wbr>Equipment<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.01]</code> <code>Share<wbr>Of<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Of<wbr>Associates<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.02]</code> <code>Unrealised<wbr>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.04]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.12]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.13]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Cash<wbr>Flow<wbr>Hedges<wbr>After<wbr>Tax</code> <i>[J1, J3, K1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (7):</b><br/><code>+</code> <code>[OCI]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.BT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.TAX]</code> <code>Tax<wbr>On<wbr>Other<wbr>Comprehensive<wbr>Income</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT.01]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Remeasurement<wbr>Of<wbr>Defined<wbr>Benefit<wbr>Obligation<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.13]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation<wbr>Before<wbr>Tax</code> <i>[J3, J4, K2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (15):</b><br/><code>+</code> <code>[OCI]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> <i>[G1, G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.02]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Remeasurement<wbr>Of<wbr>Defined<wbr>Benefit<wbr>Obligation<wbr>After<wbr>Tax</code> <i>[G1, G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.03]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> <i>[G1, G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.04]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Gains<wbr>Losses<wbr>On<wbr>Revaluation<wbr>Of<wbr>Property<wbr>And<wbr>Equipment<wbr>After<wbr>Tax</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.01]</code> <code>Share<wbr>Of<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Of<wbr>Associates<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method<wbr>After<wbr>Tax</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.02]</code> <code>Unrealised<wbr>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets<wbr>After<wbr>Tax</code> <i>[G1, G4, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.03]</code> <code>Unrealised<wbr>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Financial<wbr>Assets<wbr>After<wbr>Tax</code> <i>[G1, G4, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.04]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation<wbr>After<wbr>Tax</code> <i>[G1, G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.07]</code> <code>Reclassification<wbr>Adjustments<wbr>On<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Financial<wbr>Assets<wbr>After<wbr>Tax</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.08]</code> <code>Reclassification<wbr>Adjustments<wbr>On<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation<wbr>After<wbr>Tax</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.10]</code> <code>Reclassification<wbr>Adjustments<wbr>On<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets<wbr>After<wbr>Tax</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.12]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.13]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Cash<wbr>Flow<wbr>Hedges<wbr>After<wbr>Tax</code> <i>[G1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (16):</b><br/><code>+</code> <code>[OCI]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.BT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>Before<wbr>Tax</code> <i>[G1, G5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.TAX]</code> <code>Tax<wbr>On<wbr>Other<wbr>Comprehensive<wbr>Income</code> <i>[G1, G5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> <i>[G1, G5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> <i>[G1, G5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT.01]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Remeasurement<wbr>Of<wbr>Defined<wbr>Benefit<wbr>Obligation<wbr>Before<wbr>Tax</code> <i>[G1, G5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT.02]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT.04]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Gains<wbr>Losses<wbr>On<wbr>Revaluation<wbr>Of<wbr>Property<wbr>And<wbr>Equipment<wbr>Before<wbr>Tax</code> <i>[G1, G5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.01]</code> <code>Unrealised<wbr>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Financial<wbr>Assets<wbr>Before<wbr>Tax</code> <i>[G1, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.03]</code> <code>Reclassification<wbr>Adjustments<wbr>On<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Financial<wbr>Assets<wbr>Before<wbr>Tax</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.04]</code> <code>Unrealised<wbr>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets<wbr>Before<wbr>Tax</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.07]</code> <code>Share<wbr>Of<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Of<wbr>Associates<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method<wbr>Before<wbr>Tax</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.08]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.10]</code> <code>Reclassification<wbr>Adjustments<wbr>On<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets<wbr>Before<wbr>Tax</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.11]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Cash<wbr>Flow<wbr>Hedges<wbr>Before<wbr>Tax</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.13]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation<wbr>Before<wbr>Tax</code> <i>[G1, G5, H1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (12):</b><br/><code>+</code> <code>[OCI]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.02]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Remeasurement<wbr>Of<wbr>Defined<wbr>Benefit<wbr>Obligation<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.03]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.04]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Gains<wbr>Losses<wbr>On<wbr>Revaluation<wbr>Of<wbr>Property<wbr>And<wbr>Equipment<wbr>After<wbr>Tax</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.01]</code> <code>Share<wbr>Of<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Of<wbr>Associates<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method<wbr>After<wbr>Tax</code> <i>[E6, I2]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.02]</code> <code>Unrealised<wbr>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets<wbr>After<wbr>Tax</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.03]</code> <code>Unrealised<wbr>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Financial<wbr>Assets<wbr>After<wbr>Tax</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.04]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation<wbr>After<wbr>Tax</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.12]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.13]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Cash<wbr>Flow<wbr>Hedges<wbr>After<wbr>Tax</code> <i>[E6, G2, I2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (13):</b><br/><code>+</code> <code>[OCI]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.BT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>Before<wbr>Tax</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.TAX]</code> <code>Tax<wbr>On<wbr>Other<wbr>Comprehensive<wbr>Income</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT.01]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Remeasurement<wbr>Of<wbr>Defined<wbr>Benefit<wbr>Obligation<wbr>Before<wbr>Tax</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT.02]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.01]</code> <code>Unrealised<wbr>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Financial<wbr>Assets<wbr>Before<wbr>Tax</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.04]</code> <code>Unrealised<wbr>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets<wbr>Before<wbr>Tax</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.08]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.09]</code> <code>Reclassification<wbr>Adjustments<wbr>On<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation<wbr>Before<wbr>Tax</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.11]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Cash<wbr>Flow<wbr>Hedges<wbr>Before<wbr>Tax</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.BT.13]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation<wbr>Before<wbr>Tax</code> <i>[G5]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (14):</b><br/><code>+</code> <code>[OCI]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.02]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Remeasurement<wbr>Of<wbr>Defined<wbr>Benefit<wbr>Obligation<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.03]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.04]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Gains<wbr>Losses<wbr>On<wbr>Revaluation<wbr>Of<wbr>Property<wbr>And<wbr>Equipment<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.01]</code> <code>Share<wbr>Of<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Of<wbr>Associates<wbr>Accounted<wbr>For<wbr>Using<wbr>Equity<wbr>Method<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.02]</code> <code>Unrealised<wbr>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.03]</code> <code>Unrealised<wbr>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Financial<wbr>Assets<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.04]</code> <code>Gains<wbr>Losses<wbr>On<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.07]</code> <code>Reclassification<wbr>Adjustments<wbr>On<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>Financial<wbr>Assets<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.08]</code> <code>Reclassification<wbr>Adjustments<wbr>On<wbr>Exchange<wbr>Differences<wbr>On<wbr>Translation<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.10]</code> <code>Reclassification<wbr>Adjustments<wbr>On<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.12]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_function_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (9):</b><br/><code>+</code> <code>[OCI]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.02]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Remeasurement<wbr>Of<wbr>Defined<wbr>Benefit<wbr>Obligation<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.03]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.AT.04]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Gains<wbr>Losses<wbr>On<wbr>Revaluation<wbr>Of<wbr>Property<wbr>And<wbr>Equipment<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.02]</code> <code>Unrealised<wbr>Gains<wbr>Losses<wbr>On<wbr>Changes<wbr>In<wbr>Fair<wbr>Value<wbr>Of<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.10]</code> <code>Reclassification<wbr>Adjustments<wbr>On<wbr>Available<wbr>For<wbr>Sale<wbr>Financial<wbr>Assets<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.RC.AT.12]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>May<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>After<wbr>Tax</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_function_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (5):</b><br/><code>+</code> <code>[OCI]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>After<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.BT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT.01]</code> <code>Other<wbr>Comprehensive<wbr>Income<wbr>For<wbr>Remeasurement<wbr>Of<wbr>Defined<wbr>Benefit<wbr>Obligation<wbr>Before<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[OCI.NR.BT.02]</code> <code>Other<wbr>Adjustments<wbr>To<wbr>Other<wbr>Comprehensive<wbr>Income<wbr>That<wbr>Will<wbr>Not<wbr>Be<wbr>Reclassified<wbr>To<wbr>Profit<wbr>Or<wbr>Loss<wbr>Before<wbr>Tax</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.IS.CI]</code> <b><code>total_comprehensive_income</code></b> &nbsp;<span><i>(Total 3 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Total Laba (Rugi) Komprehensif Periode Berjalan (Konsolidasi, Induk, &amp; NCI)</b>: Gabungan Laba Bersih (<code>[PL]</code>) ditambah Penghasilan Komprehensif Lain (<code>[OCI]</code>).</td>
      <td width="34%" valign="top"><b>Direct</b>: Ambil dari <code>[CI] ComprehensiveIncome</code> dan alokasinya ke induk (<code>[CI.P]</code>) serta nonpengendali (<code>[CI.NCI]</code>).</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan total pertambahan atau pengurangan kekayaan bersih perusahaan secara utuh (Laba Bersih + OCI) dalam satu periode.<br/><b>Saran Analisis:</b> Menunjukkan perubahan nilai buku ekuitas yang sesungguhnya sebelum transaksi dividen atau aksi korporasi modal.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code>, <code>property</code>, <code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b> <code>all_variants</code><br/>• <code>by_function_after_tax</code><br/>• <code>by_function_before_tax</code><br/>• <code>by_nature_after_tax</code><br/>• <code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[CI]</code> <code>ComprehensiveIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[CI.P]</code> <code>Comprehensive<wbr>Income<wbr>Attributable<wbr>To<wbr>Parent<wbr>Entity</code> &nbsp;·&nbsp; <code>+</code> <code>[CI.NCI]</code> <code>Comprehensive<wbr>Income<wbr>Attributable<wbr>To<wbr>Non<wbr>Controlling<wbr>Interests</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code>, <code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_nature_after_tax</code><br/>• <code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[CI]</code> <code>ComprehensiveIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[CI.P]</code> <code>Comprehensive<wbr>Income<wbr>Attributable<wbr>To<wbr>Parent<wbr>Entity</code> &nbsp;·&nbsp; <code>+</code> <code>[CI.NCI]</code> <code>Comprehensive<wbr>Income<wbr>Attributable<wbr>To<wbr>Non<wbr>Controlling<wbr>Interests</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[CI]</code> <code>ComprehensiveIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[CI.P]</code> <code>Comprehensive<wbr>Income<wbr>Attributable<wbr>To<wbr>Parent<wbr>Entity</code> &nbsp;·&nbsp; <code>+</code> <code>[CI.NCI]</code> <code>Comprehensive<wbr>Income<wbr>Attributable<wbr>To<wbr>Non<wbr>Controlling<wbr>Interests</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_function_after_tax</code><br/>• <code>by_function_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[CI]</code> <code>ComprehensiveIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[CI.P]</code> <code>Comprehensive<wbr>Income<wbr>Attributable<wbr>To<wbr>Parent<wbr>Entity</code> &nbsp;·&nbsp; <code>+</code> <code>[CI.NCI]</code> <code>Comprehensive<wbr>Income<wbr>Attributable<wbr>To<wbr>Non<wbr>Controlling<wbr>Interests</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>collective_investment_contract</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>B</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>B1</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[CI]</code> <code>ComprehensiveIncome</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.IS.EPS]</code> <b><code>earnings_per_share_basic_and_diluted</code></b> &nbsp;<span><i>(Total 4 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Laba (Rugi) Bersih per Saham Dasar &amp; Dilusian (<i>Basic &amp; Diluted EPS</i>)</b>: Laba bersih pemilik induk untuk setiap 1 lembar saham beredar (dari operasi dilanjutkan maupun dihentikan).</td>
      <td width="34%" valign="top"><b>Direct</b>: Ambil dari <code>[EPS.B.C] BasicEarningsLossPerShareFromContinuingOperations</code> dan <code>[EPS.D.C] DilutedEarningsLossPerShareFromContinuingOperations</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan porsi laba bersih yang dihasilkan untuk setiap satu lembar saham yang dipegang investor publik (termasuk efek dilusi opsi/waran).<br/><b>Saran Analisis:</b> Pembagi utama terhadap harga saham untuk menghitung valuasi <b>PER (Price-to-Earnings Ratio)</b> dan memantau pertumbuhan laba per saham (<b>EPS Growth</b>).</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_function_after_tax</code><br/>• <code>by_function_before_tax</code><br/>• <code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[EPS.B.C]</code> <code>Basic<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Continuing<wbr>Operations</code> &nbsp;·&nbsp; <code>+</code> <code>[EPS.D.C]</code> <code>Diluted<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Continuing<wbr>Operations</code> &nbsp;·&nbsp; <code>+</code> <code>[EPS.B.D]</code> <code>Basic<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Discontinued<wbr>Operations</code> &nbsp;·&nbsp; <code>+</code> <code>[EPS.D.D]</code> <code>Diluted<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Discontinued<wbr>Operations</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[EPS.B.C]</code> <code>Basic<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Continuing<wbr>Operations</code> &nbsp;·&nbsp; <code>+</code> <code>[EPS.D.C]</code> <code>Diluted<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Continuing<wbr>Operations</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>C1</code>, <code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code>, <code>J3</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_function_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[EPS.B.C]</code> <code>Basic<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Continuing<wbr>Operations</code> &nbsp;·&nbsp; <code>+</code> <code>[EPS.D.C]</code> <code>Diluted<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Continuing<wbr>Operations</code> &nbsp;·&nbsp; <code>+</code> <code>[EPS.D.D]</code> <code>Diluted<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Discontinued<wbr>Operations</code> <i>[H1, J2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_function_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[EPS.B.C]</code> <code>Basic<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Continuing<wbr>Operations</code> &nbsp;·&nbsp; <code>+</code> <code>[EPS.D.C]</code> <code>Diluted<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Continuing<wbr>Operations</code> &nbsp;·&nbsp; <code>+</code> <code>[EPS.B.D]</code> <code>Basic<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Discontinued<wbr>Operations</code> <i>[G5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[EPS.D.D]</code> <code>Diluted<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Discontinued<wbr>Operations</code> <i>[H1, J2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_nature_after_tax</code><br/>• <code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[EPS.B.C]</code> <code>Basic<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Continuing<wbr>Operations</code> &nbsp;·&nbsp; <code>+</code> <code>[EPS.D.C]</code> <code>Diluted<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Continuing<wbr>Operations</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>C</code>, <code>D</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>C1</code>, <code>D1</code>, <code>D2</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_function_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[EPS.B.C]</code> <code>Basic<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Continuing<wbr>Operations</code> &nbsp;·&nbsp; <code>+</code> <code>[EPS.D.C]</code> <code>Diluted<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Continuing<wbr>Operations</code> &nbsp;·&nbsp; <code>+</code> <code>[EPS.B.D]</code> <code>Basic<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Discontinued<wbr>Operations</code> &nbsp;·&nbsp; <code>+</code> <code>[EPS.D.D]</code> <code>Diluted<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Discontinued<wbr>Operations</code> <i>[A1, J1, K2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_function_before_tax</code><br/>• <code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[EPS.B.C]</code> <code>Basic<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Continuing<wbr>Operations</code> &nbsp;·&nbsp; <code>+</code> <code>[EPS.D.C]</code> <code>Diluted<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Continuing<wbr>Operations</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[EPS.B.C]</code> <code>Basic<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Continuing<wbr>Operations</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[EPS.B.C]</code> <code>Basic<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Continuing<wbr>Operations</code> &nbsp;·&nbsp; <code>+</code> <code>[EPS.D.C]</code> <code>Diluted<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Continuing<wbr>Operations</code> &nbsp;·&nbsp; <code>+</code> <code>[EPS.B.D]</code> <code>Basic<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Discontinued<wbr>Operations</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[EPS.D.D]</code> <code>Diluted<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Discontinued<wbr>Operations</code> <i>[G1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[EPS.B.C]</code> <code>Basic<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Continuing<wbr>Operations</code> &nbsp;·&nbsp; <code>+</code> <code>[EPS.D.C]</code> <code>Diluted<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Continuing<wbr>Operations</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variants:</b><br/>• <code>by_nature_after_tax</code><br/>• <code>by_nature_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[EPS.B.C]</code> <code>Basic<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Continuing<wbr>Operations</code> &nbsp;·&nbsp; <code>+</code> <code>[EPS.D.C]</code> <code>Diluted<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Continuing<wbr>Operations</code> <i>[G2, G5]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_nature_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[EPS.B.C]</code> <code>Basic<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Continuing<wbr>Operations</code> &nbsp;·&nbsp; <code>+</code> <code>[EPS.D.C]</code> <code>Diluted<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Continuing<wbr>Operations</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_function_after_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[EPS.B.C]</code> <code>Basic<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Continuing<wbr>Operations</code> &nbsp;·&nbsp; <code>+</code> <code>[EPS.D.C]</code> <code>Diluted<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Continuing<wbr>Operations</code> &nbsp;·&nbsp; <code>+</code> <code>[EPS.B.D]</code> <code>Basic<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Discontinued<wbr>Operations</code> &nbsp;·&nbsp; <code>+</code> <code>[EPS.D.D]</code> <code>Diluted<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Discontinued<wbr>Operations</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>by_function_before_tax</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[EPS.B.C]</code> <code>Basic<wbr>Earnings<wbr>Loss<wbr>Per<wbr>Share<wbr>From<wbr>Continuing<wbr>Operations</code></td>
    </tr>
  </tbody>
</table>

---

## 3. Pemetaan Kanonik Arus Kas (`cash_flow_statement` — 14 Akun Kanonik dari 399 Akun Mentah)

### 3.1 Arus Kas dari Aktivitas Operasi Kanonik (`[CAN.CF.CFO]`)

<table width="100%">
  <colgroup>
    <col width="34%" />
    <col width="34%" />
    <col width="32%" />
  </colgroup>
  <thead>
    <tr>
      <th align="left" width="34%">Penjelasan / Entry Points / Variant</th>
      <th align="left" width="34%">Aturan Agregasi / Sectors / Accounts</th>
      <th align="left" width="32%">Makna Ekonomi &amp; Saran Analisis / Subsectors</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="3"><code>[CAN.CF.CFO]</code> <b><code>operating_cash_flow</code></b> &nbsp;<span><i>(Total 3 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Arus Kas Bersih dari Aktivitas Operasi (<i>Operating Cash Flow / OCF</i>)</b>: Total uang tunai bersih yang dihasilkan atau digunakan oleh kegiatan bisnis utama perusahaan sepanjang periode berjalan.</td>
      <td width="34%" valign="top"><b>Direct Anchor</b>: Ambil langsung dari <code>[CFO] NetCashFlowsReceivedFromUsedInOperatingActivities</code>, beserta subtotal <code>[CFO.BCA]</code> dan <code>[CFO.BCA.OPS]</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan <b>kemampuan nyata mesin bisnis menghasilkan uang tunai bersih</b> (bukan sekadar laba di atas kertas akuntansi).<br/><b>Saran Analisis:</b> Hitung <b>Cash Conversion Ratio</b> (<code>operating_cash_flow / net_income_consolidated</code>). Jika OCF terus-menerus negatif saat Laba Bersih positif pada sektor riil, itu adalah sinyal bahaya (<i>red flag</i>) manipulasi laba atau macetnya modal kerja.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[CFO]</code> <code>Net<wbr>Cash<wbr>Flows<wbr>Received<wbr>From<wbr>Used<wbr>In<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA]</code> <code>Net<wbr>Cash<wbr>Flows<wbr>Received<wbr>From<wbr>Used<wbr>In<wbr>Operating<wbr>Activities<wbr>Before<wbr>Changes<wbr>In<wbr>Assets<wbr>And<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS]</code> <code>Cash<wbr>Generated<wbr>From<wbr>Used<wbr>In<wbr>Operations</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>indirect_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[CFO]</code> <code>Net<wbr>Cash<wbr>Flows<wbr>Received<wbr>From<wbr>Used<wbr>In<wbr>Operating<wbr>Activities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code>, <code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>A</code>, <code>C</code>, <code>D</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>A1</code>, <code>C1</code>, <code>D1</code>, <code>D2</code>, <code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[CFO]</code> <code>Net<wbr>Cash<wbr>Flows<wbr>Received<wbr>From<wbr>Used<wbr>In<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS]</code> <code>Cash<wbr>Generated<wbr>From<wbr>Used<wbr>In<wbr>Operations</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code>, <code>insurance</code>, <code>collective_investment_contract</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>B</code>, <code>G</code>, <code>H</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>B1</code>, <code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[CFO]</code> <code>Net<wbr>Cash<wbr>Flows<wbr>Received<wbr>From<wbr>Used<wbr>In<wbr>Operating<wbr>Activities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[CFO]</code> <code>Net<wbr>Cash<wbr>Flows<wbr>Received<wbr>From<wbr>Used<wbr>In<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA]</code> <code>Net<wbr>Cash<wbr>Flows<wbr>Received<wbr>From<wbr>Used<wbr>In<wbr>Operating<wbr>Activities<wbr>Before<wbr>Changes<wbr>In<wbr>Assets<wbr>And<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS]</code> <code>Cash<wbr>Generated<wbr>From<wbr>Used<wbr>In<wbr>Operations</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[CFO]</code> <code>Net<wbr>Cash<wbr>Flows<wbr>Received<wbr>From<wbr>Used<wbr>In<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA]</code> <code>Net<wbr>Cash<wbr>Flows<wbr>Received<wbr>From<wbr>Used<wbr>In<wbr>Operating<wbr>Activities<wbr>Before<wbr>Changes<wbr>In<wbr>Assets<wbr>And<wbr>Liabilities</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.CF.CFO.01]</code> <b><code>cash_receipts_from_customers_and_operations</code></b> &nbsp;<span><i>(Total 35 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Penerimaan Kas dari Pelanggan &amp; Pendapatan Operasional Lintas Sektor</b>: Uang tunai masuk dari tagihan pelanggan, royalti, subsidi, bunga/bagi hasil bank, angsuran debitur multifinance, premi &amp; klaim reasuransi, komisi sekuritas, dan penjualan efek operasional.</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan seluruh akun penerimaan kas operasional <code>[CFO.BCA.OPS.IN.01-35]</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan aliran darah uang tunai masuk dari pelanggan, debitur, atau pemegang polis ke rekening kas perusahaan.<br/><b>Saran Analisis:</b> Bandingkan dengan total pendapatan di Laba Rugi; rasio penerimaan kas terhadap omzet yang mendekati 100% menunjukkan kualitas penagihan yang sangat sehat.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (7):</b><br/><code>+</code> <code>[CFO.BCA.OPS.IN.01]</code> <code>ReceiptsFromCustomers</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.02]</code> <code>Receipts<wbr>From<wbr>Royalties<wbr>Fees<wbr>Commissions<wbr>And<wbr>Other<wbr>Revenues</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.03]</code> <code>ReceiptsOfSubsidy</code> <i>[D2, G5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.04]</code> <code>ReceiptsFromInvestments</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.05]</code> <code>Receipts<wbr>From<wbr>Contracts<wbr>Held<wbr>For<wbr>Dealing<wbr>Or<wbr>Trading<wbr>Purposes</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.06]</code> <code>ReceiptFromSecuritiesCompany</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.07]</code> <code>Other<wbr>Cash<wbr>Receipts<wbr>From<wbr>Operating<wbr>Activities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>C1</code>, <code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code>, <code>J3</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[CFO.BCA.OPS.IN.01]</code> <code>ReceiptsFromCustomers</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.02]</code> <code>Receipts<wbr>From<wbr>Royalties<wbr>Fees<wbr>Commissions<wbr>And<wbr>Other<wbr>Revenues</code> <i>[61, E5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.05]</code> <code>Receipts<wbr>From<wbr>Contracts<wbr>Held<wbr>For<wbr>Dealing<wbr>Or<wbr>Trading<wbr>Purposes</code> <i>[61]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.07]</code> <code>Other<wbr>Cash<wbr>Receipts<wbr>From<wbr>Operating<wbr>Activities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>C</code>, <code>D</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>C1</code>, <code>D1</code>, <code>D2</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (5):</b><br/><code>+</code> <code>[CFO.BCA.OPS.IN.01]</code> <code>ReceiptsFromCustomers</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.02]</code> <code>Receipts<wbr>From<wbr>Royalties<wbr>Fees<wbr>Commissions<wbr>And<wbr>Other<wbr>Revenues</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.03]</code> <code>ReceiptsOfSubsidy</code> <i>[J1, J4]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.07]</code> <code>Other<wbr>Cash<wbr>Receipts<wbr>From<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.09]</code> <code>ReceiptsFromDrivers</code> <i>[K1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (11):</b><br/><code>+</code> <code>[CFO.BCA.OPS.IN.08]</code> <code>Receipts<wbr>From<wbr>Payments<wbr>To<wbr>Customers</code> <i>[G1, G4, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.10]</code> <code>Interest<wbr>From<wbr>Banks<wbr>And<wbr>Time<wbr>Deposits</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.11]</code> <code>Revenue<wbr>Receipts<wbr>From<wbr>Fund<wbr>Management<wbr>As<wbr>Mudharib</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.12]</code> <code>ReceiptsPaymentsOfCommission</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.13]</code> <code>RecoveriesOfWrittenOffAssets</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.14]</code> <code>ForeignCurrencyGainsLosses</code> <i>[G1, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.15]</code> <code>Income<wbr>From<wbr>Other<wbr>Operating<wbr>Transactions</code> <i>[G1, G5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.16]</code> <code>Receipts<wbr>From<wbr>Non<wbr>Operating<wbr>Income</code> <i>[G1, G2, G4]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.22]</code> <code>Receipts<wbr>From<wbr>Insurance<wbr>Premiums</code> <i>[G1, G4, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.23]</code> <code>Receipts<wbr>From<wbr>Reinsurance<wbr>Claims</code> <i>[G1, G4, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.32]</code> <code>Receipts<wbr>From<wbr>Payments<wbr>To<wbr>Clearing<wbr>And<wbr>Guarantee<wbr>Institution</code> <i>[G1, G5]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (5):</b><br/><code>+</code> <code>[CFO.BCA.OPS.IN.17]</code> <code>Receipts<wbr>From<wbr>Consumer<wbr>Financing</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.18]</code> <code>ReceiptsFromFinanceLeases</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.19]</code> <code>ReceiptsFromFactoring</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.20]</code> <code>Receipts<wbr>From<wbr>Loan<wbr>Channeling<wbr>And<wbr>Joint<wbr>Financing<wbr>Cooperation</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.21]</code> <code>Receipts<wbr>Of<wbr>Interest<wbr>From<wbr>Loan<wbr>Receivable</code> <i>[G2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (6):</b><br/><code>+</code> <code>[CFO.BCA.OPS.IN.22]</code> <code>Receipts<wbr>From<wbr>Insurance<wbr>Premiums</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.23]</code> <code>Receipts<wbr>From<wbr>Reinsurance<wbr>Claims</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.24]</code> <code>Receipts<wbr>From<wbr>Retrocession<wbr>Claims</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.25]</code> <code>ReceiptsFromCommission</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.26]</code> <code>ReceiptsOfInvestmentIncome</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.27]</code> <code>Receipts<wbr>From<wbr>Payments<wbr>For<wbr>Policy<wbr>Loans</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (8):</b><br/><code>+</code> <code>[CFO.BCA.OPS.IN.01]</code> <code>ReceiptsFromCustomers</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.06]</code> <code>ReceiptFromSecuritiesCompany</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.28]</code> <code>Receipts<wbr>From<wbr>Brokerage<wbr>Commissions</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.29]</code> <code>Receipts<wbr>From<wbr>Investment<wbr>Management<wbr>Fees</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.30]</code> <code>Receipts<wbr>From<wbr>Financial<wbr>Advisory<wbr>Fees</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.31]</code> <code>Receipts<wbr>From<wbr>Clearing<wbr>And<wbr>Guarantee<wbr>Institution</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.33]</code> <code>Proceeds<wbr>On<wbr>Sale<wbr>Of<wbr>Marketable<wbr>Securities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.IN.34]</code> <code>Proceeds<wbr>On<wbr>Sale<wbr>Of<wbr>Securities<wbr>Purchased<wbr>Under<wbr>Agreement<wbr>To<wbr>Resale</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>collective_investment_contract</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>B</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>B1</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[CFO.BCA.OPS.IN.35]</code> <code>Proceeds<wbr>From<wbr>Sales<wbr>Of<wbr>Equityinstrument<wbr>Portfolios</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.CF.CFO.02]</code> <b><code>cash_payments_to_suppliers_employees_and_operations</code></b> &nbsp;<span><i>(Total 31 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Pembayaran Kas kepada Pemasok, Kontraktor, Karyawan, &amp; Operasional Lintas Sektor</b>: Uang tunai keluar untuk membayar bahan baku/pemasok, gaji karyawan, kontraktor tambang/konstruksi, beban bunga/bagi hasil bank, penyaluran kredit multifinance baru, pembayaran klaim asuransi, dan transaksi kliring sekuritas.</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan seluruh akun pengeluaran kas operasional <code>[CFO.BCA.OPS.OUT.01-31]</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan pengeluaran uang tunai riil untuk membayar pemasok bahan baku, gaji karyawan, beban operasional, atau pencairan klaim.<br/><b>Saran Analisis:</b> Selisih antara <code>[CAN.CF.CFO.01]</code> dan <code>[CAN.CF.CFO.02]</code> menunjukkan <i>Cash Operating Margin</i> sebelum bunga dan pajak.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (8):</b><br/><code>+</code> <code>[CFO.BCA.OPS.OUT.01]</code> <code>Payments<wbr>To<wbr>Suppliers<wbr>For<wbr>Goods<wbr>And<wbr>Services</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.02]</code> <code>Payments<wbr>For<wbr>Salaries<wbr>And<wbr>Allowances</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.03]</code> <code>Payments<wbr>For<wbr>General<wbr>And<wbr>Administrative<wbr>Expense</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.04]</code> <code>PaymentsToContractors</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.05]</code> <code>Payments<wbr>For<wbr>Royalties<wbr>And<wbr>Exploitation<wbr>Fees</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.06]</code> <code>PaymentsForManagementFees</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.07]</code> <code>Payments<wbr>From<wbr>Contracts<wbr>Held<wbr>For<wbr>Dealing<wbr>Or<wbr>Trading<wbr>Purposes</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.08]</code> <code>Other<wbr>Cash<wbr>Payments<wbr>For<wbr>Operating<wbr>Activities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>C1</code>, <code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code>, <code>J3</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (8):</b><br/><code>+</code> <code>[CFO.BCA.OPS.OUT.01]</code> <code>Payments<wbr>To<wbr>Suppliers<wbr>For<wbr>Goods<wbr>And<wbr>Services</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.02]</code> <code>Payments<wbr>For<wbr>Salaries<wbr>And<wbr>Allowances</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.03]</code> <code>Payments<wbr>For<wbr>General<wbr>And<wbr>Administrative<wbr>Expense</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.04]</code> <code>PaymentsToContractors</code> <i>[61, H1, K1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.06]</code> <code>PaymentsForManagementFees</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.07]</code> <code>Payments<wbr>From<wbr>Contracts<wbr>Held<wbr>For<wbr>Dealing<wbr>Or<wbr>Trading<wbr>Purposes</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.08]</code> <code>Other<wbr>Cash<wbr>Payments<wbr>For<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.09]</code> <code>PaymentsForRoyalties</code> <i>[H1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>C</code>, <code>D</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>C1</code>, <code>D1</code>, <code>D2</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (5):</b><br/><code>+</code> <code>[CFO.BCA.OPS.OUT.01]</code> <code>Payments<wbr>To<wbr>Suppliers<wbr>For<wbr>Goods<wbr>And<wbr>Services</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.02]</code> <code>Payments<wbr>For<wbr>Salaries<wbr>And<wbr>Allowances</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.03]</code> <code>Payments<wbr>For<wbr>General<wbr>And<wbr>Administrative<wbr>Expense</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.04]</code> <code>PaymentsToContractors</code> <i>[J4]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.08]</code> <code>Other<wbr>Cash<wbr>Payments<wbr>For<wbr>Operating<wbr>Activities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (6):</b><br/><code>+</code> <code>[CFO.BCA.OPS.OUT.02]</code> <code>Payments<wbr>For<wbr>Salaries<wbr>And<wbr>Allowances</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.03]</code> <code>Payments<wbr>For<wbr>General<wbr>And<wbr>Administrative<wbr>Expense</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.10]</code> <code>Payments<wbr>Of<wbr>Finance<wbr>Costs<wbr>And<wbr>Bank<wbr>Administration<wbr>Charges</code> <i>[G1, G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.11]</code> <code>Payments<wbr>Of<wbr>Interests<wbr>From<wbr>Borrowings</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.12]</code> <code>Payments<wbr>Of<wbr>Temporary<wbr>Syirkah<wbr>Funds</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.13]</code> <code>Payments<wbr>For<wbr>Other<wbr>Operating<wbr>Expenses</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (5):</b><br/><code>+</code> <code>[CFO.BCA.OPS.OUT.03]</code> <code>Payments<wbr>For<wbr>General<wbr>And<wbr>Administrative<wbr>Expense</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.14]</code> <code>PaymentsForConsumerFinancing</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.15]</code> <code>PaymentsForFinanceLeases</code> <i>[C1, G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.16]</code> <code>PaymentsForFactoring</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.17]</code> <code>Payments<wbr>For<wbr>Loan<wbr>Channeling<wbr>And<wbr>Joint<wbr>Financing<wbr>Cooperation</code> <i>[E6, G2, I2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (9):</b><br/><code>+</code> <code>[CFO.BCA.OPS.OUT.02]</code> <code>Payments<wbr>For<wbr>Salaries<wbr>And<wbr>Allowances</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.03]</code> <code>Payments<wbr>For<wbr>General<wbr>And<wbr>Administrative<wbr>Expense</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.18]</code> <code>Payments<wbr>For<wbr>Insurance<wbr>Claims<wbr>And<wbr>Benefits</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.19]</code> <code>Payments<wbr>For<wbr>Reinsurance<wbr>Premiums</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.20]</code> <code>Payments<wbr>For<wbr>Retrocession<wbr>Premiums</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.21]</code> <code>PaymentsOfCommission</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.22]</code> <code>Payments<wbr>For<wbr>Other<wbr>Underwriting<wbr>Expenses</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.23]</code> <code>PaymentsForMarketingExpenses</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.24]</code> <code>Payments<wbr>For<wbr>General<wbr>And<wbr>Administrative<wbr>Expenses</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (8):</b><br/><code>+</code> <code>[CFO.BCA.OPS.OUT.01]</code> <code>Payments<wbr>To<wbr>Suppliers<wbr>For<wbr>Goods<wbr>And<wbr>Services</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.02]</code> <code>Payments<wbr>For<wbr>Salaries<wbr>And<wbr>Allowances</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.03]</code> <code>Payments<wbr>For<wbr>General<wbr>And<wbr>Administrative<wbr>Expense</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.25]</code> <code>Payments<wbr>To<wbr>Clearing<wbr>And<wbr>Guarantee<wbr>Institution</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.26]</code> <code>PaymentsToCustomers</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.27]</code> <code>PaymentsToSecuritiesCompany</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.28]</code> <code>Payments<wbr>For<wbr>Purchase<wbr>Of<wbr>Marketable<wbr>Securities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.29]</code> <code>Payments<wbr>For<wbr>Purchase<wbr>Of<wbr>Securities<wbr>Purchased<wbr>Under<wbr>Agreement<wbr>To<wbr>Resale</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>collective_investment_contract</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>B</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>B1</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[CFO.BCA.OPS.OUT.30]</code> <code>Purchase<wbr>Of<wbr>Equity<wbr>Instrument<wbr>Portfolios</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.OPS.OUT.31]</code> <code>Payments<wbr>For<wbr>Investment<wbr>Expenses</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.CF.CFO.03]</code> <b><code>operating_taxes_interest_and_dividends_cf</code></b> &nbsp;<span><i>(Total 19 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Pembayaran Pajak Penghasilan, Pita Cukai, Bunga, &amp; Dividen Operasional</b>: Setoran tunai PPh Badan, restitusi pajak, pembayaran pita cukai rokok, serta penerimaan/pembayaran bunga, dividen, dan investasi operasional sebelum perubahan modal kerja.</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan seluruh akun pajak, cukai, bunga, dan dividen pada aktivitas operasi <code>[CFO.BCA.TAX.01-19]</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan beban kas riil yang dibayarkan untuk PPh Badan, pita cukai, dan beban bunga operasional, serta bunga/dividen kas yang diterima.<br/><b>Saran Analisis:</b> Bandingkan pajak tunai yang dibayar dengan beban pajak di Laba Rugi (<code>[CAN.IS.TAX]</code>) untuk mendeteksi agresivitas pajak.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (14):</b><br/><code>+</code> <code>[CFO.BCA.TAX.01]</code> <code>Payments<wbr>For<wbr>Corporate<wbr>Income<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.02]</code> <code>Income<wbr>Taxes<wbr>Refunded<wbr>Paid<wbr>From<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.03]</code> <code>PaymentsForExcisePayable</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.04]</code> <code>Interests<wbr>Received<wbr>From<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.05]</code> <code>Interests<wbr>Paid<wbr>From<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.06]</code> <code>Dividends<wbr>Received<wbr>From<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.07]</code> <code>Dividends<wbr>Paid<wbr>From<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.08]</code> <code>Interest<wbr>Investment<wbr>Income<wbr>Fees<wbr>And<wbr>Commissions<wbr>Received</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.09]</code> <code>Payments<wbr>Of<wbr>Interest<wbr>And<wbr>Bonus<wbr>Fees<wbr>And<wbr>Commissions</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.10]</code> <code>Proceeds<wbr>From<wbr>Equity<wbr>Investments<wbr>Classified<wbr>As<wbr>Amortized<wbr>Cost<wbr>And<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income</code> <i>[A1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.11]</code> <code>Proceeds<wbr>From<wbr>Sales<wbr>Of<wbr>Investment<wbr>In<wbr>Securities</code> <i>[B1, E7, K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.12]</code> <code>Purchases<wbr>Of<wbr>Investment<wbr>In<wbr>Securities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.13]</code> <code>Repayment<wbr>Placement<wbr>Of<wbr>Refundable<wbr>Deposits</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.14]</code> <code>Other<wbr>Cash<wbr>Inflows<wbr>Outflows<wbr>From<wbr>Operating<wbr>Activities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code>, <code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>A</code>, <code>C</code>, <code>D</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>A1</code>, <code>C1</code>, <code>D1</code>, <code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (8):</b><br/><code>+</code> <code>[CFO.BCA.TAX.01]</code> <code>Payments<wbr>For<wbr>Corporate<wbr>Income<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.02]</code> <code>Income<wbr>Taxes<wbr>Refunded<wbr>Paid<wbr>From<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.04]</code> <code>Interests<wbr>Received<wbr>From<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.05]</code> <code>Interests<wbr>Paid<wbr>From<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.06]</code> <code>Dividends<wbr>Received<wbr>From<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.07]</code> <code>Dividends<wbr>Paid<wbr>From<wbr>Operating<wbr>Activities</code> <i>[H1, J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.13]</code> <code>Repayment<wbr>Placement<wbr>Of<wbr>Refundable<wbr>Deposits</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.14]</code> <code>Other<wbr>Cash<wbr>Inflows<wbr>Outflows<wbr>From<wbr>Operating<wbr>Activities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (9):</b><br/><code>+</code> <code>[CFO.BCA.TAX.01]</code> <code>Payments<wbr>For<wbr>Corporate<wbr>Income<wbr>Tax</code> <i>[G1, G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.08]</code> <code>Interest<wbr>Investment<wbr>Income<wbr>Fees<wbr>And<wbr>Commissions<wbr>Received</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.09]</code> <code>Payments<wbr>Of<wbr>Interest<wbr>And<wbr>Bonus<wbr>Fees<wbr>And<wbr>Commissions</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.10]</code> <code>Proceeds<wbr>From<wbr>Equity<wbr>Investments<wbr>Classified<wbr>As<wbr>Amortized<wbr>Cost<wbr>And<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income</code> <i>[G1, G4, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.14]</code> <code>Other<wbr>Cash<wbr>Inflows<wbr>Outflows<wbr>From<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.15]</code> <code>RefundsPaymentsOfIncomeTax</code> <i>[G1, G5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.16]</code> <code>Proceeds<wbr>From<wbr>Equity<wbr>Investments<wbr>Classified<wbr>As<wbr>Held<wbr>For<wbr>Maturity<wbr>And<wbr>Available<wbr>For<wbr>Sale</code> <i>[G1, G4, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.18]</code> <code>Payments<wbr>For<wbr>Deferred<wbr>Acquisition<wbr>Costs</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.19]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Deposits<wbr>To<wbr>Clearing<wbr>And<wbr>Guarantee<wbr>Institution</code> <i>[G5]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (5):</b><br/><code>+</code> <code>[CFO.BCA.TAX.01]</code> <code>Payments<wbr>For<wbr>Corporate<wbr>Income<wbr>Tax</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.02]</code> <code>Income<wbr>Taxes<wbr>Refunded<wbr>Paid<wbr>From<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.04]</code> <code>Interests<wbr>Received<wbr>From<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.05]</code> <code>Interests<wbr>Paid<wbr>From<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.14]</code> <code>Other<wbr>Cash<wbr>Inflows<wbr>Outflows<wbr>From<wbr>Operating<wbr>Activities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (7):</b><br/><code>+</code> <code>[CFO.BCA.TAX.01]</code> <code>Payments<wbr>For<wbr>Corporate<wbr>Income<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.02]</code> <code>Income<wbr>Taxes<wbr>Refunded<wbr>Paid<wbr>From<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.04]</code> <code>Interests<wbr>Received<wbr>From<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.05]</code> <code>Interests<wbr>Paid<wbr>From<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.13]</code> <code>Repayment<wbr>Placement<wbr>Of<wbr>Refundable<wbr>Deposits</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.14]</code> <code>Other<wbr>Cash<wbr>Inflows<wbr>Outflows<wbr>From<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.17]</code> <code>Proceeds<wbr>From<wbr>Sales<wbr>Of<wbr>Investments</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (6):</b><br/><code>+</code> <code>[CFO.BCA.TAX.01]</code> <code>Payments<wbr>For<wbr>Corporate<wbr>Income<wbr>Tax</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.02]</code> <code>Income<wbr>Taxes<wbr>Refunded<wbr>Paid<wbr>From<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.04]</code> <code>Interests<wbr>Received<wbr>From<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.05]</code> <code>Interests<wbr>Paid<wbr>From<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.14]</code> <code>Other<wbr>Cash<wbr>Inflows<wbr>Outflows<wbr>From<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.19]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Deposits<wbr>To<wbr>Clearing<wbr>And<wbr>Guarantee<wbr>Institution</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>collective_investment_contract</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>B</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>B1</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[CFO.BCA.TAX.02]</code> <code>Income<wbr>Taxes<wbr>Refunded<wbr>Paid<wbr>From<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.04]</code> <code>Interests<wbr>Received<wbr>From<wbr>Operating<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.BCA.TAX.06]</code> <code>Dividends<wbr>Received<wbr>From<wbr>Operating<wbr>Activities</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.CF.CFO.04]</code> <b><code>working_capital_and_banking_book_changes_cf</code></b> &nbsp;<span><i>(Total 49 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Perubahan Modal Kerja Operasional, Penyaluran Kredit/Pembiayaan, Penghimpunan DPK, &amp; Rekonsiliasi Metode Tidak Langsung</b>: Mutasi bersih kredit/pembiayaan syariah yang disalurkan, perubahan simpanan Giro/Tabungan/Deposito/Dana Syirkah nasabah bank, serta penyesuaian laba bersih dan modal kerja pada <i>Indirect Method</i>.</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan seluruh akun perubahan aset &amp; liabilitas operasi <code>[CFO.WC.01-41]</code> dan penyesuaian <code>[CFO.IND.01-08]</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan kas yang terserap/terbebaskan dari perubahan modal kerja (piutang, persediaan, utang usaha) atau mutasi penyaluran kredit vs penghimpunan DPK pada bank.<br/><b>Saran Analisis:</b> Menjelaskan <i>mengapa</i> Arus Kas Operasi berbeda dengan Laba Bersih (apakah kas tersedot ke penumpukan persediaan/piutang atau ekspansi kredit perbankan).</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>B</code>, <code>C</code>, <code>D</code>, <code>E</code>, <code>F</code>, <code>G</code>, <code>H</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>B1</code>, <code>C1</code>, <code>C2</code>, <code>C3</code>, <code>D1</code>, <code>D2</code>, <code>E4</code>, <code>E6</code>, <code>E7</code>, <code>F1</code>, <code>F2</code>, <code>G5</code>, <code>H1</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (5):</b><br/><code>+</code> <code>[CFO.WC.01]</code> <code>Decrease<wbr>Increase<wbr>From<wbr>Securities</code> <i>[C3, E7, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.02]</code> <code>DecreaseIncreaseFromCredit</code> <i>[C3, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.03]</code> <code>Decrease<wbr>Increase<wbr>From<wbr>Other<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.04]</code> <code>Increase<wbr>Decrease<wbr>From<wbr>Deposits<wbr>And<wbr>Deposits<wbr>From<wbr>Other<wbr>Banks</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.05]</code> <code>Increase<wbr>Decrease<wbr>From<wbr>Other<wbr>Liabilities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>indirect_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (8):</b><br/><code>+</code> <code>[CFO.IND.01]</code> <code>ProfitLoss</code> <i>[K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.IND.02]</code> <code>Depreciation<wbr>And<wbr>Amortisation<wbr>Expenses</code> <i>[K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.IND.03]</code> <code>Decrease<wbr>Increase<wbr>From<wbr>Trade<wbr>Receivables<wbr>Third<wbr>Parties</code> <i>[K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.IND.04]</code> <code>Decrease<wbr>Increase<wbr>From<wbr>Inventories</code> <i>[K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.IND.05]</code> <code>Decrease<wbr>Increase<wbr>From<wbr>Other<wbr>Current<wbr>Financial<wbr>Assets</code> <i>[K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.IND.06]</code> <code>Increase<wbr>Decrease<wbr>From<wbr>Trade<wbr>Payables<wbr>Third<wbr>Parties</code> <i>[K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.IND.07]</code> <code>Increase<wbr>Decrease<wbr>From<wbr>Other<wbr>Payables<wbr>Third<wbr>Parties</code> <i>[K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFO.IND.08]</code> <code>Increase<wbr>Decrease<wbr>From<wbr>Other<wbr>Payables<wbr>Related<wbr>Parties</code> <i>[K2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (36):</b><br/><code>+</code> <code>[CFO.WC.06]</code> <code>Decrease<wbr>Increase<wbr>In<wbr>Placements<wbr>With<wbr>Other<wbr>Banks<wbr>And<wbr>Bank<wbr>Indonesia</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.07]</code> <code>Decrease<wbr>Increase<wbr>In<wbr>Marketable<wbr>Securities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.08]</code> <code>Decrease<wbr>Increase<wbr>In<wbr>Securities<wbr>Purchased<wbr>Under<wbr>Resale<wbr>Agreements</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.09]</code> <code>Decrease<wbr>Increase<wbr>In<wbr>Derivative<wbr>Receivables</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.10]</code> <code>DecreaseIncreaseInLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.11]</code> <code>Decrease<wbr>Increase<wbr>In<wbr>Consumer<wbr>Financing<wbr>Receivables</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.12]</code> <code>Decrease<wbr>Increase<wbr>In<wbr>Lease<wbr>Investments</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.13]</code> <code>DecreaseIncreaseInFactoring</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.14]</code> <code>Decrease<wbr>Increase<wbr>In<wbr>Acceptance<wbr>Receivables</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.15]</code> <code>Decrease<wbr>Increase<wbr>In<wbr>Bills<wbr>And<wbr>Other<wbr>Receivables</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.16]</code> <code>Decrease<wbr>Increase<wbr>In<wbr>Murabahah<wbr>Receivables</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.17]</code> <code>Decrease<wbr>Increase<wbr>In<wbr>Istishna<wbr>Receivables</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.18]</code> <code>Decrease<wbr>Increase<wbr>In<wbr>Ijarah<wbr>Receivables</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.19]</code> <code>Decrease<wbr>Increase<wbr>In<wbr>Ijarah<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.20]</code> <code>DecreaseIncreaseInQardhFunds</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.21]</code> <code>Decrease<wbr>Increase<wbr>In<wbr>Mudharabah<wbr>Financing</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.22]</code> <code>Decrease<wbr>Increase<wbr>In<wbr>Musyarakah<wbr>Financing</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.23]</code> <code>Decrease<wbr>Increase<wbr>In<wbr>Foreclosed<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.24]</code> <code>Decrease<wbr>Increase<wbr>In<wbr>Other<wbr>Receivables</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.25]</code> <code>Decrease<wbr>Increase<wbr>In<wbr>Other<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.26]</code> <code>Increase<wbr>Decrease<wbr>In<wbr>Obligations<wbr>Due<wbr>Immediately</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.27]</code> <code>Increase<wbr>Decrease<wbr>In<wbr>Customers<wbr>Current<wbr>Accounts<wbr>And<wbr>Savings</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.28]</code> <code>Increase<wbr>Decrease<wbr>In<wbr>Customers<wbr>Time<wbr>Deposits</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.29]</code> <code>Increase<wbr>Decrease<wbr>In<wbr>Other<wbr>Banks<wbr>Saving<wbr>Deposits</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.30]</code> <code>Increase<wbr>Decrease<wbr>In<wbr>Securities<wbr>Sold<wbr>Under<wbr>Repurchase<wbr>Agreement</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.31]</code> <code>Increase<wbr>Decrease<wbr>In<wbr>Derivative<wbr>Payables</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.32]</code> <code>Increase<wbr>Decrease<wbr>In<wbr>Acceptance<wbr>Payables</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.33]</code> <code>Increase<wbr>Decrease<wbr>In<wbr>Securities<wbr>Issued</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.34]</code> <code>Increase<wbr>Decrease<wbr>In<wbr>Liabilities<wbr>To<wbr>Policyholder<wbr>On<wbr>Unit<wbr>Linked<wbr>Contracts</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.35]</code> <code>Increase<wbr>Decrease<wbr>In<wbr>Other<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.36]</code> <code>Increase<wbr>Decrease<wbr>In<wbr>Customers<wbr>Wadiah<wbr>Demand<wbr>Deposits</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.37]</code> <code>Increase<wbr>Decrease<wbr>In<wbr>Customers<wbr>Wadiah<wbr>Saving<wbr>Deposits</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.38]</code> <code>Increase<wbr>Decrease<wbr>In<wbr>Customers<wbr>Wakalah<wbr>Deposits</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.39]</code> <code>Increase<wbr>Decrease<wbr>In<wbr>Mudharabah<wbr>Current<wbr>Account</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.40]</code> <code>Increase<wbr>Decrease<wbr>In<wbr>Mudharabah<wbr>Savings<wbr>Deposits</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.41]</code> <code>Increase<wbr>Decrease<wbr>In<wbr>Temporary<wbr>Syirkah<wbr>Funds</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G2</code>, <code>G5</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (5):</b><br/><code>+</code> <code>[CFO.WC.01]</code> <code>Decrease<wbr>Increase<wbr>From<wbr>Securities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.02]</code> <code>DecreaseIncreaseFromCredit</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.03]</code> <code>Decrease<wbr>Increase<wbr>From<wbr>Other<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.04]</code> <code>Increase<wbr>Decrease<wbr>From<wbr>Deposits<wbr>And<wbr>Deposits<wbr>From<wbr>Other<wbr>Banks</code> &nbsp;·&nbsp; <code>+</code> <code>[CFO.WC.05]</code> <code>Increase<wbr>Decrease<wbr>From<wbr>Other<wbr>Liabilities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[CFO.WC.01]</code> <code>Decrease<wbr>Increase<wbr>From<wbr>Securities</code></td>
    </tr>
  </tbody>
</table>

### 3.2 Arus Kas dari Aktivitas Investasi Kanonik (`[CAN.CF.CFI]`)

<table width="100%">
  <colgroup>
    <col width="34%" />
    <col width="34%" />
    <col width="32%" />
  </colgroup>
  <thead>
    <tr>
      <th align="left" width="34%">Penjelasan / Entry Points / Variant</th>
      <th align="left" width="34%">Aturan Agregasi / Sectors / Accounts</th>
      <th align="left" width="32%">Makna Ekonomi &amp; Saran Analisis / Subsectors</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="3"><code>[CAN.CF.CFI]</code> <b><code>investing_cash_flow</code></b> &nbsp;<span><i>(Total 1 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Arus Kas Bersih dari Aktivitas Investasi (<i>Investing Cash Flow / CFI</i>)</b>: Total kas masuk/keluar bersih dari belanja modal (<i>CapEx</i>), penempatan/pencairan investasi keuangan, serta akuisisi/pelepasan anak usaha.</td>
      <td width="34%" valign="top"><b>Direct Anchor</b>: Ambil langsung dari <code>[CFI] NetCashFlowsReceivedFromUsedInInvestingActivities</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan strategi alokasi modal jangka panjang manajemen — apakah sedang agresif berekspansi atau sedang menjual aset untuk bertahan hidup.<br/><b>Saran Analisis:</b> Perusahaan tumbuh yang sehat lazimnya memiliki CFI negatif (karena belanja <i>CapEx</i>), yang dibiayai dari arus kas operasi (OCF) yang positif.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b> <code>all_variants</code><br/>• <code>direct_method</code><br/>• <code>indirect_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[CFI]</code> <code>Net<wbr>Cash<wbr>Flows<wbr>Received<wbr>From<wbr>Used<wbr>In<wbr>Investing<wbr>Activities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code>, <code>infrastructure</code>, <code>financial_and_sharia</code>, <code>financing</code>, <code>insurance</code>, <code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>A</code>, <code>C</code>, <code>D</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>I</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>A1</code>, <code>C1</code>, <code>D1</code>, <code>D2</code>, <code>E3</code>, <code>E5</code>, <code>E6</code>, <code>G1</code>, <code>G2</code>, <code>G3</code>, <code>G4</code>, <code>G5</code>, <code>H1</code>, <code>I2</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[CFI]</code> <code>Net<wbr>Cash<wbr>Flows<wbr>Received<wbr>From<wbr>Used<wbr>In<wbr>Investing<wbr>Activities</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.CF.CFI.01]</code> <b><code>capital_expenditures_and_real_asset_disposals</code></b> &nbsp;<span><i>(Total 34 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Belanja Modal (<i>Capital Expenditure / CapEx</i>) &amp; Hasil Pelepasan Aset Riil</b>: Pembelian/pembangunan pabrik, mesin, gedung, perangkat TI, kebun sawit, HTI, ternak indukan, properti tambang, sumur migas, pengupasan tanah tangguhan, dan jalan tol, serta kas masuk dari penjualannya.</td>
      <td width="34%" valign="top"><b>CapEx Outflow / Net</b>: Jumlahkan seluruh akun pembayaran perolehan aset tetap &amp; sektoral <code>PaymentsForAcquisitionOf...</code> sebagai <b>Total CapEx</b>, dan akun <code>ProceedsFromDisposalOf...</code> sebagai hasil pelepasan aset.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan <b>investasi belanja modal (<i>CapEx</i>)</b> untuk meremajakan dan memperbesar kapasitas pabrik, mesin, kebun, tambang, atau infrastruktur.<br/><b>Saran Analisis:</b> Kurangkan pengeluaran CapEx dari <code>operating_cash_flow</code> untuk menghitung <b>Free Cash Flow (FCF)</b>. Jika CapEx lebih kecil dari beban penyusutan (D&amp;A), kapasitas fisik perusahaan sedang menyusut (<i>under-investment</i>).</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (27):</b><br/><code>+</code> <code>[CFI.CAPEX.01]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Property<wbr>Plant<wbr>And<wbr>Equipment</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.02]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Property<wbr>Plant<wbr>And<wbr>Equipment</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.03]</code> <code>Payments<wbr>For<wbr>Advances<wbr>For<wbr>Purchase<wbr>Of<wbr>Property<wbr>Plant<wbr>And<wbr>Equipment</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.04]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Intangible<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.05]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Intangible<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.06]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Investment<wbr>Properties</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.07]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Investment<wbr>Properties</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.08]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Land<wbr>For<wbr>Development</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.09]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Land<wbr>For<wbr>Development</code> <i>[B1, C3, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.10]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Plantation<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.11]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Plantation<wbr>Assets</code> <i>[D2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.12]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Plasma<wbr>Plantations</code> <i>[B1, D2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.13]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Plasma<wbr>Plantations</code> <i>[B1, D2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.14]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Industrial<wbr>Timber<wbr>Plantations</code> <i>[B1, D2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.15]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Industrial<wbr>Timber<wbr>Plantations</code> <i>[B1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.16]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Livestock<wbr>Production</code> <i>[D2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.17]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Livestock<wbr>Production</code> <i>[D2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.18]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Mining<wbr>Properties</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.19]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Mining<wbr>Properties</code> <i>[A1, B1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.20]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Exploration<wbr>And<wbr>Evaluation<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.21]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Exploration<wbr>And<wbr>Evaluation<wbr>Assets</code> <i>[A1, B1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.22]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Oil<wbr>And<wbr>Gas<wbr>Assets</code> <i>[A1, E2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.23]</code> <code>Payments<wbr>For<wbr>Deferred<wbr>Stripping<wbr>Costs</code> <i>[A1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.24]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Toll<wbr>Road<wbr>Concession<wbr>Rights</code> <i>[C3, F2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.25]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Other<wbr>Non<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.26]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Other<wbr>Non<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.27]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Foreclosed<wbr>Assets</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>indirect_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[CFI.CAPEX.01]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Property<wbr>Plant<wbr>And<wbr>Equipment</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.03]</code> <code>Payments<wbr>For<wbr>Advances<wbr>For<wbr>Purchase<wbr>Of<wbr>Property<wbr>Plant<wbr>And<wbr>Equipment</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>C1</code>, <code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code>, <code>J3</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (11):</b><br/><code>+</code> <code>[CFI.CAPEX.04]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Intangible<wbr>Assets</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.05]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Intangible<wbr>Assets</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.06]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Investment<wbr>Properties</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.07]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Investment<wbr>Properties</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.08]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Land<wbr>For<wbr>Development</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.09]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Land<wbr>For<wbr>Development</code> <i>[E5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.25]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Other<wbr>Non<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.26]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Other<wbr>Non<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.28]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Property<wbr>And<wbr>Equipment</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.29]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Property<wbr>And<wbr>Equipment</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.30]</code> <code>Payments<wbr>For<wbr>Advances<wbr>For<wbr>Purchase<wbr>Of<wbr>Property<wbr>And<wbr>Equipment</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>C</code>, <code>D</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>C1</code>, <code>D1</code>, <code>D2</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (11):</b><br/><code>+</code> <code>[CFI.CAPEX.04]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Intangible<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.05]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Intangible<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.06]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Investment<wbr>Properties</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.07]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Investment<wbr>Properties</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.24]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Toll<wbr>Road<wbr>Concession<wbr>Rights</code> <i>[J1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.25]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Other<wbr>Non<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.26]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Other<wbr>Non<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.28]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Property<wbr>And<wbr>Equipment</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.29]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Property<wbr>And<wbr>Equipment</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.30]</code> <code>Payments<wbr>For<wbr>Advances<wbr>For<wbr>Purchase<wbr>Of<wbr>Property<wbr>And<wbr>Equipment</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.34]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Toll<wbr>Road<wbr>Concession<wbr>Rights</code> <i>[J2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[CFI.CAPEX.31]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Acquisition<wbr>Of<wbr>Property<wbr>And<wbr>Equipment</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.32]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Acquisition<wbr>Of<wbr>Investment<wbr>Properties</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.33]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Acquisition<wbr>Of<wbr>Intangible<wbr>Assets<wbr>Other<wbr>Than<wbr>Goodwill</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (7):</b><br/><code>+</code> <code>[CFI.CAPEX.06]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Investment<wbr>Properties</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.07]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Investment<wbr>Properties</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.25]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Other<wbr>Non<wbr>Financial<wbr>Assets</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.26]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Other<wbr>Non<wbr>Financial<wbr>Assets</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.27]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Foreclosed<wbr>Assets</code> <i>[C1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.28]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Property<wbr>And<wbr>Equipment</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.29]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Property<wbr>And<wbr>Equipment</code> <i>[C1, G2, G5]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (7):</b><br/><code>+</code> <code>[CFI.CAPEX.04]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Intangible<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.06]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Investment<wbr>Properties</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.07]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Investment<wbr>Properties</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.25]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Other<wbr>Non<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.26]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Other<wbr>Non<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.28]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Property<wbr>And<wbr>Equipment</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.29]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Property<wbr>And<wbr>Equipment</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (8):</b><br/><code>+</code> <code>[CFI.CAPEX.04]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Intangible<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.05]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Intangible<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.06]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Investment<wbr>Properties</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.07]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Investment<wbr>Properties</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.25]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Other<wbr>Non<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.26]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Other<wbr>Non<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.28]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Property<wbr>And<wbr>Equipment</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.CAPEX.29]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Property<wbr>And<wbr>Equipment</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.CF.CFI.02]</code> <b><code>financial_investments_and_related_party_loans_cf</code></b> &nbsp;<span><i>(Total 26 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Penempatan/Pencairan Investasi Keuangan &amp; Pemberian/Pelunasan Pinjaman Pihak Berelasi</b>: Mutasi deposito &gt; 3 bulan, jual-beli surat berharga/obligasi investasi, dana dibatasi penggunaannya, serta arus kas pinjaman kepada pihak berelasi/pemegang saham.</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan seluruh akun <code>[CFI.FIN.01-26]</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan arus kas penempatan/pencairan instrumen keuangan dan aliran pinjaman kas keluar/masuk kepada pihak berelasi.<br/><b>Saran Analisis:</b> Waspadai kas keluar besar ke <code>PaymentsOfReceivablesFromRelatedParties</code> yang mengindikasikan uang perusahaan disedot untuk membiayai grup afiliasi.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (23):</b><br/><code>+</code> <code>[CFI.FIN.01]</code> <code>PaymentsForDeferredCharges</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.02]</code> <code>Payments<wbr>For<wbr>Deferred<wbr>Mobilisation<wbr>Costs</code> <i>[E7]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.03]</code> <code>Receipts<wbr>From<wbr>Payments<wbr>For<wbr>Aircraft<wbr>Maintenance<wbr>Funds</code> <i>[K1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.04]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Short<wbr>Term<wbr>Investments</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.05]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Financial<wbr>Assets<wbr>At<wbr>Fair<wbr>Value<wbr>Through<wbr>Profit<wbr>Or<wbr>Loss</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.06]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Financial<wbr>Assets<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.07]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Financial<wbr>Assets<wbr>Available<wbr>For<wbr>Sale</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.08]</code> <code>Placement<wbr>Of<wbr>Financial<wbr>Assets<wbr>Amortized<wbr>Cost<wbr>Investments</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.09]</code> <code>Withdrawal<wbr>Of<wbr>Financial<wbr>Assets<wbr>Amortized<wbr>Cost<wbr>Investments</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.10]</code> <code>Placement<wbr>Of<wbr>Financial<wbr>Assets<wbr>Held<wbr>To<wbr>Maturity<wbr>Investments</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.11]</code> <code>Withdrawal<wbr>Of<wbr>Financial<wbr>Assets<wbr>Held<wbr>To<wbr>Maturity<wbr>Investments</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.12]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Bonds<wbr>And<wbr>Or<wbr>Sukuk</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.13]</code> <code>Payments<wbr>To<wbr>Acquire<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.14]</code> <code>Proceeds<wbr>On<wbr>Sale<wbr>Of<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.15]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Restricted<wbr>Funds<wbr>From<wbr>Investing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.16]</code> <code>Receipts<wbr>From<wbr>Future<wbr>Contracts<wbr>Forward<wbr>Contracts<wbr>Option<wbr>Contracts<wbr>And<wbr>Swap<wbr>Contracts</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.17]</code> <code>Payments<wbr>For<wbr>Future<wbr>Contracts<wbr>Forward<wbr>Contracts<wbr>Option<wbr>Contracts<wbr>And<wbr>Swap<wbr>Contracts</code> <i>[D2, E1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.18]</code> <code>Payments<wbr>Of<wbr>Receivables<wbr>From<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.19]</code> <code>Receipts<wbr>From<wbr>Receivables<wbr>From<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.20]</code> <code>Payments<wbr>Of<wbr>Receivables<wbr>From<wbr>Stockholders</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.21]</code> <code>Receipts<wbr>From<wbr>Receivables<wbr>From<wbr>Stockholders</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.22]</code> <code>Cash<wbr>Advances<wbr>And<wbr>Loans<wbr>Made<wbr>To<wbr>Other<wbr>Parties<wbr>Other<wbr>Than<wbr>Financing<wbr>Institutions</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.23]</code> <code>Cash<wbr>Receipts<wbr>From<wbr>The<wbr>Repayment<wbr>Of<wbr>Advances<wbr>And<wbr>Loans<wbr>Made<wbr>To<wbr>Other<wbr>Parties<wbr>Other<wbr>Than<wbr>Financing</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>C1</code>, <code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (18):</b><br/><code>+</code> <code>[CFI.FIN.04]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Short<wbr>Term<wbr>Investments</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.05]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Financial<wbr>Assets<wbr>At<wbr>Fair<wbr>Value<wbr>Through<wbr>Profit<wbr>Or<wbr>Loss</code> <i>[E5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.06]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Financial<wbr>Assets<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income</code> <i>[H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.07]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Financial<wbr>Assets<wbr>Available<wbr>For<wbr>Sale</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.08]</code> <code>Placement<wbr>Of<wbr>Financial<wbr>Assets<wbr>Amortized<wbr>Cost<wbr>Investments</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.09]</code> <code>Withdrawal<wbr>Of<wbr>Financial<wbr>Assets<wbr>Amortized<wbr>Cost<wbr>Investments</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.10]</code> <code>Placement<wbr>Of<wbr>Financial<wbr>Assets<wbr>Held<wbr>To<wbr>Maturity<wbr>Investments</code> <i>[61, E5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.11]</code> <code>Withdrawal<wbr>Of<wbr>Financial<wbr>Assets<wbr>Held<wbr>To<wbr>Maturity<wbr>Investments</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.13]</code> <code>Payments<wbr>To<wbr>Acquire<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.14]</code> <code>Proceeds<wbr>On<wbr>Sale<wbr>Of<wbr>Financial<wbr>Assets</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.15]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Restricted<wbr>Funds<wbr>From<wbr>Investing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.16]</code> <code>Receipts<wbr>From<wbr>Future<wbr>Contracts<wbr>Forward<wbr>Contracts<wbr>Option<wbr>Contracts<wbr>And<wbr>Swap<wbr>Contracts</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.17]</code> <code>Payments<wbr>For<wbr>Future<wbr>Contracts<wbr>Forward<wbr>Contracts<wbr>Option<wbr>Contracts<wbr>And<wbr>Swap<wbr>Contracts</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.18]</code> <code>Payments<wbr>Of<wbr>Receivables<wbr>From<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.19]</code> <code>Receipts<wbr>From<wbr>Receivables<wbr>From<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.21]</code> <code>Receipts<wbr>From<wbr>Receivables<wbr>From<wbr>Stockholders</code> <i>[E5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.22]</code> <code>Cash<wbr>Advances<wbr>And<wbr>Loans<wbr>Made<wbr>To<wbr>Other<wbr>Parties<wbr>Other<wbr>Than<wbr>Financing<wbr>Institutions</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.23]</code> <code>Cash<wbr>Receipts<wbr>From<wbr>The<wbr>Repayment<wbr>Of<wbr>Advances<wbr>And<wbr>Loans<wbr>Made<wbr>To<wbr>Other<wbr>Parties<wbr>Other<wbr>Than<wbr>Financing</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>D</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>D1</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (20):</b><br/><code>+</code> <code>[CFI.FIN.01]</code> <code>PaymentsForDeferredCharges</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.04]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Short<wbr>Term<wbr>Investments</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.05]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Financial<wbr>Assets<wbr>At<wbr>Fair<wbr>Value<wbr>Through<wbr>Profit<wbr>Or<wbr>Loss</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.06]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Financial<wbr>Assets<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.07]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Financial<wbr>Assets<wbr>Available<wbr>For<wbr>Sale</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.08]</code> <code>Placement<wbr>Of<wbr>Financial<wbr>Assets<wbr>Amortized<wbr>Cost<wbr>Investments</code> <i>[J1, J2, J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.09]</code> <code>Withdrawal<wbr>Of<wbr>Financial<wbr>Assets<wbr>Amortized<wbr>Cost<wbr>Investments</code> <i>[J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.10]</code> <code>Placement<wbr>Of<wbr>Financial<wbr>Assets<wbr>Held<wbr>To<wbr>Maturity<wbr>Investments</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.11]</code> <code>Withdrawal<wbr>Of<wbr>Financial<wbr>Assets<wbr>Held<wbr>To<wbr>Maturity<wbr>Investments</code> <i>[A1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.13]</code> <code>Payments<wbr>To<wbr>Acquire<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.14]</code> <code>Proceeds<wbr>On<wbr>Sale<wbr>Of<wbr>Financial<wbr>Assets</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.15]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Restricted<wbr>Funds<wbr>From<wbr>Investing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.16]</code> <code>Receipts<wbr>From<wbr>Future<wbr>Contracts<wbr>Forward<wbr>Contracts<wbr>Option<wbr>Contracts<wbr>And<wbr>Swap<wbr>Contracts</code> <i>[K1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.17]</code> <code>Payments<wbr>For<wbr>Future<wbr>Contracts<wbr>Forward<wbr>Contracts<wbr>Option<wbr>Contracts<wbr>And<wbr>Swap<wbr>Contracts</code> <i>[J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.18]</code> <code>Payments<wbr>Of<wbr>Receivables<wbr>From<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.19]</code> <code>Receipts<wbr>From<wbr>Receivables<wbr>From<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.21]</code> <code>Receipts<wbr>From<wbr>Receivables<wbr>From<wbr>Stockholders</code> <i>[J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.22]</code> <code>Cash<wbr>Advances<wbr>And<wbr>Loans<wbr>Made<wbr>To<wbr>Other<wbr>Parties<wbr>Other<wbr>Than<wbr>Financing<wbr>Institutions</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.23]</code> <code>Cash<wbr>Receipts<wbr>From<wbr>The<wbr>Repayment<wbr>Of<wbr>Advances<wbr>And<wbr>Loans<wbr>Made<wbr>To<wbr>Other<wbr>Parties<wbr>Other<wbr>Than<wbr>Financing</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.24]</code> <code>Receipts<wbr>Payments<wbr>For<wbr>Aircraft<wbr>Maintenance<wbr>Funds</code> <i>[K1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G4</code>, <code>G5</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (6):</b><br/><code>+</code> <code>[CFI.FIN.06]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Financial<wbr>Assets<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.08]</code> <code>Placement<wbr>Of<wbr>Financial<wbr>Assets<wbr>Amortized<wbr>Cost<wbr>Investments</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.09]</code> <code>Withdrawal<wbr>Of<wbr>Financial<wbr>Assets<wbr>Amortized<wbr>Cost<wbr>Investments</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.12]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Bonds<wbr>And<wbr>Or<wbr>Sukuk</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.25]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Marketable<wbr>Securities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.26]</code> <code>Placement<wbr>Of<wbr>Certificate<wbr>Of<wbr>Mudharabah<wbr>Investments</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[CFI.FIN.06]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Financial<wbr>Assets<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[CFI.FIN.06]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Financial<wbr>Assets<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.08]</code> <code>Placement<wbr>Of<wbr>Financial<wbr>Assets<wbr>Amortized<wbr>Cost<wbr>Investments</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.09]</code> <code>Withdrawal<wbr>Of<wbr>Financial<wbr>Assets<wbr>Amortized<wbr>Cost<wbr>Investments</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[CFI.FIN.06]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Financial<wbr>Assets<wbr>Fair<wbr>Value<wbr>Through<wbr>Other<wbr>Comprehensive<wbr>Income</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.FIN.15]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Restricted<wbr>Funds<wbr>From<wbr>Investing<wbr>Activities</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.CF.CFI.03]</code> <b><code>mergers_acquisitions_and_investing_returns_cf</code></b> &nbsp;<span><i>(Total 16 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Akuisisi/Divestasi Anak Usaha, Asosiasi, JV, &amp; Penerimaan Dividen/Bunga Investasi</b>: Kas keluar untuk membeli perusahaan baru (M&amp;A), kas masuk dari menjual anak usaha/asosiasi, serta dividen dan bunga tunai yang diterima dari portofolio investasi.</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan seluruh akun <code>[CFI.MA.01-11]</code> dan <code>[CFI.OTH.01-05]</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan aktivitas ekspansi anorganik (akuisisi/divestasi anak usaha) serta setoran dividen/bunga tunai dari entitas asosiasi/investasi.<br/><b>Saran Analisis:</b> Bandingkan dividen tunai yang diterima di sini dengan laba metode ekuitas (<code>[CAN.IS.EQ]</code>) untuk menguji kualitas kas investasi asosiasi.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (15):</b><br/><code>+</code> <code>[CFI.MA.01]</code> <code>Payments<wbr>For<wbr>Advances<wbr>On<wbr>Investments</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.02]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Subsidiaries</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.03]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Subsidiaries</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.04]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Additional<wbr>Interests<wbr>In<wbr>Subsidiaries</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.05]</code> <code>Proceeds<wbr>From<wbr>Sales<wbr>Of<wbr>Interests<wbr>In<wbr>Subsidiaries<wbr>Without<wbr>Loss<wbr>Of<wbr>Control<wbr>From<wbr>Investing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.06]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Interests<wbr>In<wbr>Associates</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.07]</code> <code>Proceeds<wbr>From<wbr>Sales<wbr>Of<wbr>Interests<wbr>In<wbr>Associates</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.08]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Interests<wbr>In<wbr>Joint<wbr>Ventures</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.09]</code> <code>Proceeds<wbr>From<wbr>Sales<wbr>Of<wbr>Interests<wbr>In<wbr>Joint<wbr>Ventures</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.10]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Non<wbr>Current<wbr>Assets<wbr>Or<wbr>Disposal<wbr>Groups<wbr>Classified<wbr>As<wbr>Held<wbr>For<wbr>Sale<wbr>And<wbr>Discontinued<wbr>Operations</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.OTH.01]</code> <code>Dividends<wbr>Received<wbr>From<wbr>Investing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.OTH.02]</code> <code>Interests<wbr>Received<wbr>From<wbr>Investing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.OTH.03]</code> <code>Interests<wbr>Paid<wbr>From<wbr>Investing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.OTH.04]</code> <code>Income<wbr>Taxes<wbr>Refunded<wbr>Paid<wbr>From<wbr>Investing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.OTH.05]</code> <code>Other<wbr>Cash<wbr>Inflows<wbr>Outflows<wbr>From<wbr>Investing<wbr>Activities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>C1</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code>, <code>J3</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (14):</b><br/><code>+</code> <code>[CFI.MA.01]</code> <code>Payments<wbr>For<wbr>Advances<wbr>On<wbr>Investments</code> <i>[G5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.02]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Subsidiaries</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.03]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Subsidiaries</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.04]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Additional<wbr>Interests<wbr>In<wbr>Subsidiaries</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.05]</code> <code>Proceeds<wbr>From<wbr>Sales<wbr>Of<wbr>Interests<wbr>In<wbr>Subsidiaries<wbr>Without<wbr>Loss<wbr>Of<wbr>Control<wbr>From<wbr>Investing<wbr>Activities</code> <i>[H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.06]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Interests<wbr>In<wbr>Associates</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.07]</code> <code>Proceeds<wbr>From<wbr>Sales<wbr>Of<wbr>Interests<wbr>In<wbr>Associates</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.08]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Interests<wbr>In<wbr>Joint<wbr>Ventures</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.09]</code> <code>Proceeds<wbr>From<wbr>Sales<wbr>Of<wbr>Interests<wbr>In<wbr>Joint<wbr>Ventures</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.10]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Non<wbr>Current<wbr>Assets<wbr>Or<wbr>Disposal<wbr>Groups<wbr>Classified<wbr>As<wbr>Held<wbr>For<wbr>Sale<wbr>And<wbr>Discontinued<wbr>Operations</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.OTH.01]</code> <code>Dividends<wbr>Received<wbr>From<wbr>Investing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.OTH.02]</code> <code>Interests<wbr>Received<wbr>From<wbr>Investing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.OTH.04]</code> <code>Income<wbr>Taxes<wbr>Refunded<wbr>Paid<wbr>From<wbr>Investing<wbr>Activities</code> <i>[H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.OTH.05]</code> <code>Other<wbr>Cash<wbr>Inflows<wbr>Outflows<wbr>From<wbr>Investing<wbr>Activities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>D</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>D2</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (14):</b><br/><code>+</code> <code>[CFI.MA.02]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Subsidiaries</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.03]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Subsidiaries</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.04]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Additional<wbr>Interests<wbr>In<wbr>Subsidiaries</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.05]</code> <code>Proceeds<wbr>From<wbr>Sales<wbr>Of<wbr>Interests<wbr>In<wbr>Subsidiaries<wbr>Without<wbr>Loss<wbr>Of<wbr>Control<wbr>From<wbr>Investing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.06]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Interests<wbr>In<wbr>Associates</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.07]</code> <code>Proceeds<wbr>From<wbr>Sales<wbr>Of<wbr>Interests<wbr>In<wbr>Associates</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.08]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Interests<wbr>In<wbr>Joint<wbr>Ventures</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.09]</code> <code>Proceeds<wbr>From<wbr>Sales<wbr>Of<wbr>Interests<wbr>In<wbr>Joint<wbr>Ventures</code> <i>[J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.10]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Non<wbr>Current<wbr>Assets<wbr>Or<wbr>Disposal<wbr>Groups<wbr>Classified<wbr>As<wbr>Held<wbr>For<wbr>Sale<wbr>And<wbr>Discontinued<wbr>Operations</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.OTH.01]</code> <code>Dividends<wbr>Received<wbr>From<wbr>Investing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.OTH.02]</code> <code>Interests<wbr>Received<wbr>From<wbr>Investing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.OTH.03]</code> <code>Interests<wbr>Paid<wbr>From<wbr>Investing<wbr>Activities</code> <i>[J1, J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.OTH.04]</code> <code>Income<wbr>Taxes<wbr>Refunded<wbr>Paid<wbr>From<wbr>Investing<wbr>Activities</code> <i>[A1, J1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.OTH.05]</code> <code>Other<wbr>Cash<wbr>Inflows<wbr>Outflows<wbr>From<wbr>Investing<wbr>Activities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (8):</b><br/><code>+</code> <code>[CFI.MA.02]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Subsidiaries</code> <i>[G1, G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.04]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Additional<wbr>Interests<wbr>In<wbr>Subsidiaries</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.05]</code> <code>Proceeds<wbr>From<wbr>Sales<wbr>Of<wbr>Interests<wbr>In<wbr>Subsidiaries<wbr>Without<wbr>Loss<wbr>Of<wbr>Control<wbr>From<wbr>Investing<wbr>Activities</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.06]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Interests<wbr>In<wbr>Associates</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.07]</code> <code>Proceeds<wbr>From<wbr>Sales<wbr>Of<wbr>Interests<wbr>In<wbr>Associates</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.11]</code> <code>Proceeds<wbr>From<wbr>Sales<wbr>Of<wbr>Subsidiaries</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.OTH.01]</code> <code>Dividends<wbr>Received<wbr>From<wbr>Investing<wbr>Activities</code> <i>[G1, G5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.OTH.05]</code> <code>Other<wbr>Cash<wbr>Inflows<wbr>Outflows<wbr>From<wbr>Investing<wbr>Activities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (9):</b><br/><code>+</code> <code>[CFI.MA.02]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Subsidiaries</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.03]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Subsidiaries</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.04]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Additional<wbr>Interests<wbr>In<wbr>Subsidiaries</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.06]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Interests<wbr>In<wbr>Associates</code> <i>[G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.07]</code> <code>Proceeds<wbr>From<wbr>Sales<wbr>Of<wbr>Interests<wbr>In<wbr>Associates</code> <i>[G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.10]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Non<wbr>Current<wbr>Assets<wbr>Or<wbr>Disposal<wbr>Groups<wbr>Classified<wbr>As<wbr>Held<wbr>For<wbr>Sale<wbr>And<wbr>Discontinued<wbr>Operations</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.OTH.01]</code> <code>Dividends<wbr>Received<wbr>From<wbr>Investing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.OTH.02]</code> <code>Interests<wbr>Received<wbr>From<wbr>Investing<wbr>Activities</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFI.OTH.05]</code> <code>Other<wbr>Cash<wbr>Inflows<wbr>Outflows<wbr>From<wbr>Investing<wbr>Activities</code> <i>[G2, G5]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (5):</b><br/><code>+</code> <code>[CFI.OTH.01]</code> <code>Dividends<wbr>Received<wbr>From<wbr>Investing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.OTH.02]</code> <code>Interests<wbr>Received<wbr>From<wbr>Investing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.OTH.03]</code> <code>Interests<wbr>Paid<wbr>From<wbr>Investing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.OTH.04]</code> <code>Income<wbr>Taxes<wbr>Refunded<wbr>Paid<wbr>From<wbr>Investing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.OTH.05]</code> <code>Other<wbr>Cash<wbr>Inflows<wbr>Outflows<wbr>From<wbr>Investing<wbr>Activities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (6):</b><br/><code>+</code> <code>[CFI.MA.02]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Subsidiaries</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.03]</code> <code>Proceeds<wbr>From<wbr>Disposal<wbr>Of<wbr>Subsidiaries</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.06]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Interests<wbr>In<wbr>Associates</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.MA.07]</code> <code>Proceeds<wbr>From<wbr>Sales<wbr>Of<wbr>Interests<wbr>In<wbr>Associates</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.OTH.02]</code> <code>Interests<wbr>Received<wbr>From<wbr>Investing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFI.OTH.05]</code> <code>Other<wbr>Cash<wbr>Inflows<wbr>Outflows<wbr>From<wbr>Investing<wbr>Activities</code></td>
    </tr>
  </tbody>
</table>

### 3.3 Arus Kas dari Aktivitas Pendanaan (`[CAN.CF.CFF]`) & Rekonsiliasi Kas (`[CAN.CF.CFS]`)

<table width="100%">
  <colgroup>
    <col width="34%" />
    <col width="34%" />
    <col width="32%" />
  </colgroup>
  <thead>
    <tr>
      <th align="left" width="34%">Penjelasan / Entry Points / Variant</th>
      <th align="left" width="34%">Aturan Agregasi / Sectors / Accounts</th>
      <th align="left" width="32%">Makna Ekonomi &amp; Saran Analisis / Subsectors</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="3"><code>[CAN.CF.CFF]</code> <b><code>financing_cash_flow</code></b> &nbsp;<span><i>(Total 1 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Arus Kas Bersih dari Aktivitas Pendanaan (<i>Financing Cash Flow / CFF</i>)</b>: Total kas masuk/keluar bersih dari penarikan/pelunasan pinjaman dan surat utang, penerbitan saham/unit KIK, <i>buyback</i> saham, dan pembayaran dividen.</td>
      <td width="34%" valign="top"><b>Direct Anchor</b>: Ambil langsung dari <code>[CFF] NetCashFlowsReceivedFromUsedInFinancingActivities</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan bagaimana perusahaan menutup defisit kasnya (lewat utang/saham baru) atau mendistribusikan surplus kasnya kepada kreditur dan pemegang saham.<br/><b>Saran Analisis:</b> CFF negatif pada perusahaan dengan OCF kuat menandakan fase <i>deleveraging</i> (pelunasan utang) dan pembagian dividen yang sehat; sebaliknya CFF positif terus-menerus saat OCF negatif menandakan perusahaan hidup dari gali lubang tutup lubang utang.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b> <code>all_variants</code><br/>• <code>direct_method</code><br/>• <code>indirect_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[CFF]</code> <code>Net<wbr>Cash<wbr>Flows<wbr>Received<wbr>From<wbr>Used<wbr>In<wbr>Financing<wbr>Activities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code>, <code>infrastructure</code>, <code>financial_and_sharia</code>, <code>financing</code>, <code>insurance</code>, <code>securities</code>, <code>collective_investment_contract</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>A1</code>, <code>B1</code>, <code>C1</code>, <code>D1</code>, <code>D2</code>, <code>E3</code>, <code>E5</code>, <code>E6</code>, <code>G1</code>, <code>G2</code>, <code>G3</code>, <code>G4</code>, <code>G5</code>, <code>H1</code>, <code>I2</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[CFF]</code> <code>Net<wbr>Cash<wbr>Flows<wbr>Received<wbr>From<wbr>Used<wbr>In<wbr>Financing<wbr>Activities</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.CF.CFF.01]</code> <b><code>debt_issuance_and_repayments_cf</code></b> &nbsp;<span><i>(Total 51 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Pencairan (<i>Proceeds</i>) &amp; Pelunasan (<i>Payments</i>) Utang Berbunga Lintas Sektor</b>: Kas masuk dari penarikan pinjaman bank, penerbitan obligasi, sukuk, MTN, wesel bayar, dan pinjaman subordinasi dikurangi kas keluar untuk pelunasan pokok utang, cicilan sewa pembiayaan (PSAK 73), dan biaya emisi surat utang.</td>
      <td width="34%" valign="top"><b>Net Borrowing (Proceeds − Payments)</b>: Jumlahkan seluruh akun pencairan utang <code>ProceedsFrom... / IssuanceOf...</code> dan kurangkan dengan <code>PaymentsOf... / PaymentsForBorrowings</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan siklus penarikan utang baru (<i>drawdown/issuance</i>) vs pembayaran kembali pokok pinjaman, obligasi, dan sewa pembiayaan.<br/><b>Saran Analisis:</b> Hitung <b>Net Borrowing</b> (pencairan dikurangi pelunasan) untuk melihat apakah perusahaan sedang menambah atau memangkas beban utang pokoknya.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (39):</b><br/><code>+</code> <code>[CFF.DEBT.01]</code> <code>ProceedsFromBankLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.02]</code> <code>PaymentsOfBankLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.03]</code> <code>ProceedsFromBondsPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.04]</code> <code>PaymentsOfBondsPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.05]</code> <code>ProceedsFromSukuk</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.06]</code> <code>PaymentsOfSukuk</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.07]</code> <code>ProceedsFromMediumTermNotes</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.08]</code> <code>PaymentsOfMediumTermNotes</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.09]</code> <code>ProceedsFromNotesPayable</code> <i>[A1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.10]</code> <code>PaymentsOfNotesPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.11]</code> <code>Proceeds<wbr>From<wbr>Convertible<wbr>Bonds<wbr>Issuance</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.12]</code> <code>PaymentsOfConvertibleBonds</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.13]</code> <code>SubordinatedBondsIssued</code> <i>[E7, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.14]</code> <code>PaymentsOfBondsIssuanceCosts</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.15]</code> <code>Proceeds<wbr>From<wbr>Finance<wbr>Lease<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.16]</code> <code>Payments<wbr>Of<wbr>Finance<wbr>Lease<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.17]</code> <code>Proceeds<wbr>From<wbr>Consumer<wbr>Financing<wbr>Payables</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.18]</code> <code>Payments<wbr>Of<wbr>Consumer<wbr>Financing<wbr>Payables</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.19]</code> <code>Proceeds<wbr>From<wbr>Non-Bank<wbr>Financial<wbr>Institution<wbr>Loan</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.20]</code> <code>Payments<wbr>Of<wbr>Non-Bank<wbr>Financial<wbr>Institution<wbr>Loan</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.21]</code> <code>ProceedsFromSecuredLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.22]</code> <code>PaymentsOfSecuredLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.23]</code> <code>ProceedsFromUnsecuredLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.24]</code> <code>PaymentsOfUnsecuredLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.25]</code> <code>ProceedsFromStepLoans</code> <i>[F2, I1, K1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.26]</code> <code>PaymentsOfStepLoans</code> <i>[B1, K1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.27]</code> <code>Proceeds<wbr>From<wbr>Subordinated<wbr>Loans</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.28]</code> <code>PaymentsOfSubordinatedLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.29]</code> <code>ProceedsFromOtherBorrowings</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.30]</code> <code>PaymentsOfOtherBorrowings</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.31]</code> <code>Proceeds<wbr>From<wbr>Due<wbr>To<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.32]</code> <code>Payments<wbr>Of<wbr>Due<wbr>To<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.33]</code> <code>Proceeds<wbr>From<wbr>Due<wbr>To<wbr>Stockholders</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.34]</code> <code>PaymentsOfDueToStockholders</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.35]</code> <code>Proceeds<wbr>From<wbr>Joint<wbr>Operation<wbr>Liabilities</code> <i>[B1, D2, E5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.36]</code> <code>Payments<wbr>Of<wbr>Joint<wbr>Operation<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.37]</code> <code>Proceeds<wbr>From<wbr>Retention<wbr>Payables</code> <i>[A1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.38]</code> <code>PaymentsOfRetentionPayables</code> <i>[B1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.39]</code> <code>Proceeds<wbr>From<wbr>Electricity<wbr>Purchase<wbr>Payables</code> <i>[C1, D2]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>indirect_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[CFF.DEBT.17]</code> <code>Proceeds<wbr>From<wbr>Consumer<wbr>Financing<wbr>Payables</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.18]</code> <code>Payments<wbr>Of<wbr>Consumer<wbr>Financing<wbr>Payables</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.19]</code> <code>Proceeds<wbr>From<wbr>Non-Bank<wbr>Financial<wbr>Institution<wbr>Loan</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>C1</code>, <code>E3</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code>, <code>J3</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (31):</b><br/><code>+</code> <code>[CFF.DEBT.01]</code> <code>ProceedsFromBankLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.02]</code> <code>PaymentsOfBankLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.03]</code> <code>ProceedsFromBondsPayable</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.04]</code> <code>PaymentsOfBondsPayable</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.05]</code> <code>ProceedsFromSukuk</code> <i>[H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.06]</code> <code>PaymentsOfSukuk</code> <i>[E5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.07]</code> <code>ProceedsFromMediumTermNotes</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.08]</code> <code>PaymentsOfMediumTermNotes</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.09]</code> <code>ProceedsFromNotesPayable</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.10]</code> <code>PaymentsOfNotesPayable</code> <i>[61, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.11]</code> <code>Proceeds<wbr>From<wbr>Convertible<wbr>Bonds<wbr>Issuance</code> <i>[E5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.12]</code> <code>PaymentsOfConvertibleBonds</code> <i>[E5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.13]</code> <code>SubordinatedBondsIssued</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.14]</code> <code>PaymentsOfBondsIssuanceCosts</code> <i>[E5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.15]</code> <code>Proceeds<wbr>From<wbr>Finance<wbr>Lease<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.16]</code> <code>Payments<wbr>Of<wbr>Finance<wbr>Lease<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.19]</code> <code>Proceeds<wbr>From<wbr>Non-Bank<wbr>Financial<wbr>Institution<wbr>Loan</code> <i>[E5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.20]</code> <code>Payments<wbr>Of<wbr>Non-Bank<wbr>Financial<wbr>Institution<wbr>Loan</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.21]</code> <code>ProceedsFromSecuredLoans</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.22]</code> <code>PaymentsOfSecuredLoans</code> <i>[61, E5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.23]</code> <code>ProceedsFromUnsecuredLoans</code> <i>[H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.24]</code> <code>PaymentsOfUnsecuredLoans</code> <i>[61, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.27]</code> <code>Proceeds<wbr>From<wbr>Subordinated<wbr>Loans</code> <i>[61, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.28]</code> <code>PaymentsOfSubordinatedLoans</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.29]</code> <code>ProceedsFromOtherBorrowings</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.30]</code> <code>PaymentsOfOtherBorrowings</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.31]</code> <code>Proceeds<wbr>From<wbr>Due<wbr>To<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.32]</code> <code>Payments<wbr>Of<wbr>Due<wbr>To<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.33]</code> <code>Proceeds<wbr>From<wbr>Due<wbr>To<wbr>Stockholders</code> <i>[61, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.34]</code> <code>PaymentsOfDueToStockholders</code> <i>[61, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.38]</code> <code>PaymentsOfRetentionPayables</code> <i>[61, H1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>C</code>, <code>D</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>C1</code>, <code>D1</code>, <code>D2</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (35):</b><br/><code>+</code> <code>[CFF.DEBT.01]</code> <code>ProceedsFromBankLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.02]</code> <code>PaymentsOfBankLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.03]</code> <code>ProceedsFromBondsPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.04]</code> <code>PaymentsOfBondsPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.05]</code> <code>ProceedsFromSukuk</code> <i>[J2, J3, K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.06]</code> <code>PaymentsOfSukuk</code> <i>[J2, J3, K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.07]</code> <code>ProceedsFromMediumTermNotes</code> <i>[J2, J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.08]</code> <code>PaymentsOfMediumTermNotes</code> <i>[A1, J2, J3]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.09]</code> <code>ProceedsFromNotesPayable</code> <i>[J4]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.10]</code> <code>PaymentsOfNotesPayable</code> <i>[J4]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.11]</code> <code>Proceeds<wbr>From<wbr>Convertible<wbr>Bonds<wbr>Issuance</code> <i>[J3, K1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.12]</code> <code>PaymentsOfConvertibleBonds</code> <i>[J3, K1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.14]</code> <code>PaymentsOfBondsIssuanceCosts</code> <i>[J2, J3, J4]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.15]</code> <code>Proceeds<wbr>From<wbr>Finance<wbr>Lease<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.16]</code> <code>Payments<wbr>Of<wbr>Finance<wbr>Lease<wbr>Liabilities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.17]</code> <code>Proceeds<wbr>From<wbr>Consumer<wbr>Financing<wbr>Payables</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.18]</code> <code>Payments<wbr>Of<wbr>Consumer<wbr>Financing<wbr>Payables</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.19]</code> <code>Proceeds<wbr>From<wbr>Non-Bank<wbr>Financial<wbr>Institution<wbr>Loan</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.20]</code> <code>Payments<wbr>Of<wbr>Non-Bank<wbr>Financial<wbr>Institution<wbr>Loan</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.21]</code> <code>ProceedsFromSecuredLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.22]</code> <code>PaymentsOfSecuredLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.23]</code> <code>ProceedsFromUnsecuredLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.24]</code> <code>PaymentsOfUnsecuredLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.26]</code> <code>PaymentsOfStepLoans</code> <i>[J4]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.27]</code> <code>Proceeds<wbr>From<wbr>Subordinated<wbr>Loans</code> <i>[J1, J3, K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.28]</code> <code>PaymentsOfSubordinatedLoans</code> <i>[A1, J1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.29]</code> <code>ProceedsFromOtherBorrowings</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.30]</code> <code>PaymentsOfOtherBorrowings</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.31]</code> <code>Proceeds<wbr>From<wbr>Due<wbr>To<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.32]</code> <code>Payments<wbr>Of<wbr>Due<wbr>To<wbr>Related<wbr>Parties</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.33]</code> <code>Proceeds<wbr>From<wbr>Due<wbr>To<wbr>Stockholders</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.34]</code> <code>PaymentsOfDueToStockholders</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.35]</code> <code>Proceeds<wbr>From<wbr>Joint<wbr>Operation<wbr>Liabilities</code> <i>[J1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.36]</code> <code>Payments<wbr>Of<wbr>Joint<wbr>Operation<wbr>Liabilities</code> <i>[J1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.51]</code> <code>Payments<wbr>Of<wbr>Loan<wbr>From<wbr>Government<wbr>Of<wbr>The<wbr>Republic<wbr>Of<wbr>Indonesia</code> <i>[J1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (14):</b><br/><code>+</code> <code>[CFF.DEBT.04]</code> <code>PaymentsOfBondsPayable</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.07]</code> <code>ProceedsFromMediumTermNotes</code> <i>[G2, G4]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.08]</code> <code>PaymentsOfMediumTermNotes</code> <i>[G1, G4]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.13]</code> <code>SubordinatedBondsIssued</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.14]</code> <code>PaymentsOfBondsIssuanceCosts</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.27]</code> <code>Proceeds<wbr>From<wbr>Subordinated<wbr>Loans</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.28]</code> <code>PaymentsOfSubordinatedLoans</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.40]</code> <code>ProceedsFromBorrowings</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.41]</code> <code>PaymentsForBorrowings</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.42]</code> <code>ProceedsFromBondsIssuance</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.43]</code> <code>PaymentsOfSubordinatedBonds</code> <i>[G1, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.44]</code> <code>Subordinated<wbr>Bonds<wbr>Issuance<wbr>Costs</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.45]</code> <code>IssuanceOfMudharabahSukuk</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.47]</code> <code>Issuance<wbr>Cost<wbr>Of<wbr>Mudharabah<wbr>Sukuk</code> <i>[G1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G2</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (19):</b><br/><code>+</code> <code>[CFF.DEBT.01]</code> <code>ProceedsFromBankLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.02]</code> <code>PaymentsOfBankLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.07]</code> <code>ProceedsFromMediumTermNotes</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.08]</code> <code>PaymentsOfMediumTermNotes</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.13]</code> <code>SubordinatedBondsIssued</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.14]</code> <code>PaymentsOfBondsIssuanceCosts</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.16]</code> <code>Payments<wbr>Of<wbr>Finance<wbr>Lease<wbr>Liabilities</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.19]</code> <code>Proceeds<wbr>From<wbr>Non-Bank<wbr>Financial<wbr>Institution<wbr>Loan</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.20]</code> <code>Payments<wbr>Of<wbr>Non-Bank<wbr>Financial<wbr>Institution<wbr>Loan</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.27]</code> <code>Proceeds<wbr>From<wbr>Subordinated<wbr>Loans</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.28]</code> <code>PaymentsOfSubordinatedLoans</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.29]</code> <code>ProceedsFromOtherBorrowings</code> <i>[C1, G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.30]</code> <code>PaymentsOfOtherBorrowings</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.43]</code> <code>PaymentsOfSubordinatedBonds</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.45]</code> <code>IssuanceOfMudharabahSukuk</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.46]</code> <code>PaymentsOfMudharabahSukuk</code> <i>[G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.48]</code> <code>ProceedsFromDebtSecurities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.49]</code> <code>PaymentsOfDebtSecurities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.50]</code> <code>Payments<wbr>Of<wbr>Debt<wbr>Securities<wbr>Issuance<wbr>Costs</code> <i>[G2, G5]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (10):</b><br/><code>+</code> <code>[CFF.DEBT.01]</code> <code>ProceedsFromBankLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.02]</code> <code>PaymentsOfBankLoans</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.03]</code> <code>ProceedsFromBondsPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.04]</code> <code>PaymentsOfBondsPayable</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.07]</code> <code>ProceedsFromMediumTermNotes</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.08]</code> <code>PaymentsOfMediumTermNotes</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.19]</code> <code>Proceeds<wbr>From<wbr>Non-Bank<wbr>Financial<wbr>Institution<wbr>Loan</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.20]</code> <code>Payments<wbr>Of<wbr>Non-Bank<wbr>Financial<wbr>Institution<wbr>Loan</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.27]</code> <code>Proceeds<wbr>From<wbr>Subordinated<wbr>Loans</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DEBT.28]</code> <code>PaymentsOfSubordinatedLoans</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.CF.CFF.02]</code> <b><code>equity_issuance_buyback_and_kik_units_cf</code></b> &nbsp;<span><i>(Total 15 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Penerbitan Saham (IPO / Rights Issue), Pembelian Kembali Saham (<i>Share Buyback</i>), &amp; Transaksi Unit Penyertaan KIK</b>: Dana segar dari penerbitan saham baru, setoran modal, ESOP, transaksi saham anak usaha tanpa kehilangan kendali, <i>buyback</i> saham treasuri, serta <i>subscription/redemption</i> unit KIK.</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan seluruh akun transaksi modal ekuitas <code>[CFF.EQ.01-15]</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan penggalangan modal ekuitas baru (IPO, <i>Rights Issue</i>) vs pengembalian modal lewat pembelian kembali saham (<i>Share Buyback</i>).<br/><b>Saran Analisis:</b> Emisi saham berulang kali tanpa pertumbuhan laba per saham (EPS) menyebabkan dilusi kepemilikan investor publik.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (10):</b><br/><code>+</code> <code>[CFF.EQ.01]</code> <code>Proceeds<wbr>From<wbr>Issuance<wbr>Of<wbr>Common<wbr>Stocks</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.02]</code> <code>Proceeds<wbr>From<wbr>Issuance<wbr>Of<wbr>Preferred<wbr>Stocks</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.03]</code> <code>Proceeds<wbr>From<wbr>Issuing<wbr>Other<wbr>Equity<wbr>Instruments</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.04]</code> <code>PaymentsOfStockIssuanceCosts</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.05]</code> <code>Proceeds<wbr>From<wbr>Sales<wbr>Purchases<wbr>Of<wbr>Treasury<wbr>Stocks</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.06]</code> <code>Proceeds<wbr>From<wbr>Employee<wbr>Stock<wbr>Options<wbr>Program</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.07]</code> <code>Proceed<wbr>From<wbr>Increase<wbr>Of<wbr>Non<wbr>Controlling<wbr>Interest</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.08]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Noncontrolling<wbr>Interests<wbr>In<wbr>Subsidiaries</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.09]</code> <code>Proceeds<wbr>From<wbr>Sales<wbr>Of<wbr>Interests<wbr>In<wbr>Subsidiaries<wbr>Without<wbr>Loss<wbr>Of<wbr>Control<wbr>From<wbr>Financing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.10]</code> <code>Settlement<wbr>Placement<wbr>Of<wbr>Derivative<wbr>Transactions</code> <i>[A1, B1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>indirect_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (1):</b><br/><code>+</code> <code>[CFF.EQ.01]</code> <code>Proceeds<wbr>From<wbr>Issuance<wbr>Of<wbr>Common<wbr>Stocks</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>C1</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J2</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (9):</b><br/><code>+</code> <code>[CFF.EQ.01]</code> <code>Proceeds<wbr>From<wbr>Issuance<wbr>Of<wbr>Common<wbr>Stocks</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.02]</code> <code>Proceeds<wbr>From<wbr>Issuance<wbr>Of<wbr>Preferred<wbr>Stocks</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.03]</code> <code>Proceeds<wbr>From<wbr>Issuing<wbr>Other<wbr>Equity<wbr>Instruments</code> <i>[E5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.04]</code> <code>PaymentsOfStockIssuanceCosts</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.05]</code> <code>Proceeds<wbr>From<wbr>Sales<wbr>Purchases<wbr>Of<wbr>Treasury<wbr>Stocks</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.07]</code> <code>Proceed<wbr>From<wbr>Increase<wbr>Of<wbr>Non<wbr>Controlling<wbr>Interest</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.08]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Noncontrolling<wbr>Interests<wbr>In<wbr>Subsidiaries</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.09]</code> <code>Proceeds<wbr>From<wbr>Sales<wbr>Of<wbr>Interests<wbr>In<wbr>Subsidiaries<wbr>Without<wbr>Loss<wbr>Of<wbr>Control<wbr>From<wbr>Financing<wbr>Activities</code> <i>[H1, J2, K1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.10]</code> <code>Settlement<wbr>Placement<wbr>Of<wbr>Derivative<wbr>Transactions</code> <i>[H1]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>D</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>D1</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (10):</b><br/><code>+</code> <code>[CFF.EQ.01]</code> <code>Proceeds<wbr>From<wbr>Issuance<wbr>Of<wbr>Common<wbr>Stocks</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.02]</code> <code>Proceeds<wbr>From<wbr>Issuance<wbr>Of<wbr>Preferred<wbr>Stocks</code> <i>[J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.03]</code> <code>Proceeds<wbr>From<wbr>Issuing<wbr>Other<wbr>Equity<wbr>Instruments</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.04]</code> <code>PaymentsOfStockIssuanceCosts</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.05]</code> <code>Proceeds<wbr>From<wbr>Sales<wbr>Purchases<wbr>Of<wbr>Treasury<wbr>Stocks</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.06]</code> <code>Proceeds<wbr>From<wbr>Employee<wbr>Stock<wbr>Options<wbr>Program</code> <i>[J3, J4]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.07]</code> <code>Proceed<wbr>From<wbr>Increase<wbr>Of<wbr>Non<wbr>Controlling<wbr>Interest</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.08]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Noncontrolling<wbr>Interests<wbr>In<wbr>Subsidiaries</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.09]</code> <code>Proceeds<wbr>From<wbr>Sales<wbr>Of<wbr>Interests<wbr>In<wbr>Subsidiaries<wbr>Without<wbr>Loss<wbr>Of<wbr>Control<wbr>From<wbr>Financing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.10]</code> <code>Settlement<wbr>Placement<wbr>Of<wbr>Derivative<wbr>Transactions</code> <i>[J3]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (6):</b><br/><code>+</code> <code>[CFF.EQ.04]</code> <code>PaymentsOfStockIssuanceCosts</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.06]</code> <code>Proceeds<wbr>From<wbr>Employee<wbr>Stock<wbr>Options<wbr>Program</code> <i>[G1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.07]</code> <code>Proceed<wbr>From<wbr>Increase<wbr>Of<wbr>Non<wbr>Controlling<wbr>Interest</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.11]</code> <code>Proceeds<wbr>From<wbr>Issuance<wbr>Of<wbr>New<wbr>Stocks</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.12]</code> <code>Proceeds<wbr>From<wbr>Capital<wbr>Contributions</code> <i>[G1, G2, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.13]</code> <code>Sales<wbr>Purchase<wbr>Of<wbr>Treasury<wbr>Stocks</code> <i>[G1, G5]</i></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G2</code>, <code>G5</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[CFF.EQ.01]</code> <code>Proceeds<wbr>From<wbr>Issuance<wbr>Of<wbr>Common<wbr>Stocks</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.03]</code> <code>Proceeds<wbr>From<wbr>Issuing<wbr>Other<wbr>Equity<wbr>Instruments</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.04]</code> <code>PaymentsOfStockIssuanceCosts</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.07]</code> <code>Proceed<wbr>From<wbr>Increase<wbr>Of<wbr>Non<wbr>Controlling<wbr>Interest</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>G4</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[CFF.EQ.01]</code> <code>Proceeds<wbr>From<wbr>Issuance<wbr>Of<wbr>Common<wbr>Stocks</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.04]</code> <code>PaymentsOfStockIssuanceCosts</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.07]</code> <code>Proceed<wbr>From<wbr>Increase<wbr>Of<wbr>Non<wbr>Controlling<wbr>Interest</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[CFF.EQ.04]</code> <code>PaymentsOfStockIssuanceCosts</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.07]</code> <code>Proceed<wbr>From<wbr>Increase<wbr>Of<wbr>Non<wbr>Controlling<wbr>Interest</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>collective_investment_contract</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>B</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>B1</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[CFF.EQ.14]</code> <code>Proceeds<wbr>From<wbr>Sales<wbr>Of<wbr>Participation<wbr>Unit</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.EQ.15]</code> <code>Payments<wbr>For<wbr>Acquisition<wbr>Of<wbr>Participation<wbr>Unit</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.CF.CFF.03]</code> <b><code>dividends_and_financing_interest_paid_cf</code></b> &nbsp;<span><i>(Total 6 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Pembayaran Dividen Tunai &amp; Bunga Pendanaan</b>: Uang tunai yang dibayarkan kepada pemegang saham sebagai dividen serta pembayaran bunga atas fasilitas pendanaan.</td>
      <td width="34%" valign="top"><b>Sum</b>: Jumlahkan seluruh akun dividen dan bunga pendanaan <code>[CFF.DIV.01-06]</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan <b>komitmen pengembalian uang tunai nyata (dividen kas)</b> kepada pemegang saham induk dan minoritas.<br/><b>Saran Analisis:</b> Bandingkan dengan <code>Free Cash Flow</code>; jika perusahaan membayar dividen besar padahal FCF negatif, berarti dividen tersebut dibayar menggunakan uang pinjaman utang baru.</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (6):</b><br/><code>+</code> <code>[CFF.DIV.01]</code> <code>Dividends<wbr>Paid<wbr>From<wbr>Financing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DIV.02]</code> <code>Interests<wbr>Paid<wbr>From<wbr>Financing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DIV.03]</code> <code>Interests<wbr>Received<wbr>From<wbr>Financing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DIV.04]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Restricted<wbr>Funds<wbr>From<wbr>Financing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DIV.05]</code> <code>Income<wbr>Taxes<wbr>Refunded<wbr>Paid<wbr>From<wbr>Financing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DIV.06]</code> <code>Other<wbr>Cash<wbr>Inflows<wbr>Outflows<wbr>From<wbr>Financing<wbr>Activities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>indirect_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[CFF.DIV.01]</code> <code>Dividends<wbr>Paid<wbr>From<wbr>Financing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DIV.04]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Restricted<wbr>Funds<wbr>From<wbr>Financing<wbr>Activities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code>, <code>infrastructure</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>C</code>, <code>D</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>C1</code>, <code>D2</code>, <code>E5</code>, <code>G5</code>, <code>H1</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (6):</b><br/><code>+</code> <code>[CFF.DIV.01]</code> <code>Dividends<wbr>Paid<wbr>From<wbr>Financing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DIV.02]</code> <code>Interests<wbr>Paid<wbr>From<wbr>Financing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DIV.03]</code> <code>Interests<wbr>Received<wbr>From<wbr>Financing<wbr>Activities</code> <i>[H1, J2, K2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DIV.04]</code> <code>Withdrawal<wbr>Placement<wbr>Of<wbr>Restricted<wbr>Funds<wbr>From<wbr>Financing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DIV.05]</code> <code>Income<wbr>Taxes<wbr>Refunded<wbr>Paid<wbr>From<wbr>Financing<wbr>Activities</code> <i>[E5, H1, J2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DIV.06]</code> <code>Other<wbr>Cash<wbr>Inflows<wbr>Outflows<wbr>From<wbr>Financing<wbr>Activities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code>, <code>H</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[CFF.DIV.01]</code> <code>Dividends<wbr>Paid<wbr>From<wbr>Financing<wbr>Activities</code> <i>[G1, G5, H1]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DIV.06]</code> <code>Other<wbr>Cash<wbr>Inflows<wbr>Outflows<wbr>From<wbr>Financing<wbr>Activities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financing</code>, <code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>A</code>, <code>C</code>, <code>E</code>, <code>G</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>A1</code>, <code>C1</code>, <code>E6</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[CFF.DIV.01]</code> <code>Dividends<wbr>Paid<wbr>From<wbr>Financing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DIV.02]</code> <code>Interests<wbr>Paid<wbr>From<wbr>Financing<wbr>Activities</code> <i>[G2, G4, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DIV.03]</code> <code>Interests<wbr>Received<wbr>From<wbr>Financing<wbr>Activities</code> <i>[G4, G5]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DIV.06]</code> <code>Other<wbr>Cash<wbr>Inflows<wbr>Outflows<wbr>From<wbr>Financing<wbr>Activities</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (3):</b><br/><code>+</code> <code>[CFF.DIV.01]</code> <code>Dividends<wbr>Paid<wbr>From<wbr>Financing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DIV.02]</code> <code>Interests<wbr>Paid<wbr>From<wbr>Financing<wbr>Activities</code> &nbsp;·&nbsp; <code>+</code> <code>[CFF.DIV.06]</code> <code>Other<wbr>Cash<wbr>Inflows<wbr>Outflows<wbr>From<wbr>Financing<wbr>Activities</code></td>
    </tr>
    <tr>
      <td colspan="3">&nbsp;</td>
    </tr>
    <tr>
      <td colspan="3"><code>[CAN.CF.CFS]</code> <b><code>net_change_and_ending_cash_reconciliation</code></b> &nbsp;<span><i>(Total 5 akun mentah lintas sektor)</i></span></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Perubahan Bersih Kas, Efek Selisih Kurs Kas, &amp; Saldo Akhir Kas pada Laporan Arus Kas</b>: Rekonsiliasi dari kenaikan/penurunan bersih kas (<code>[CFO] + [CFI] + [CFF]</code>), penyesuaian selisih kurs valas, dan dekonsolidasi anak usaha menuju saldo akhir kas.</td>
      <td width="34%" valign="top"><b>Reconciliation</b>: <code>Beginning Cash + NetIncreaseDecreaseInCashAndCashEquivalents + EffectOfExchangeRateChangesOnCashAndCashEquivalents + OtherAdjustments = CashAndCashEquivalentsCashFlows (Ending)</code>.</td>
      <td width="32%" valign="top"><b>Apa yang Digambarkan:</b> Menggambarkan pertambahan/penurunan kas bersih sepanjang periode berjalan dan menjembatani saldo kas awal ke saldo kas akhir.<br/><b>Saran Analisis:</b> <b>Validasi Lintas Laporan:</b> Saldo kas akhir di baris ini wajib cocok dengan posisi kas di Neraca (<code>[CAN.BS.A.01]</code>).</td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>general</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>all_sectors</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>all_subsectors</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (5):</b><br/><code>+</code> <code>[CFS.NET]</code> <code>Net<wbr>Increase<wbr>Decrease<wbr>In<wbr>Cash<wbr>And<wbr>Cash<wbr>Equivalents</code> &nbsp;·&nbsp; <code>+</code> <code>[CFS.FX]</code> <code>Effect<wbr>Of<wbr>Exchange<wbr>Rate<wbr>Changes<wbr>On<wbr>Cash<wbr>And<wbr>Cash<wbr>Equivalents</code> &nbsp;·&nbsp; <code>+</code> <code>[CFS.DEC]</code> <code>Cash<wbr>And<wbr>Cash<wbr>Equivalent<wbr>Of<wbr>Deconsolidated<wbr>Subsidiaries</code> &nbsp;·&nbsp; <code>+</code> <code>[CFS.OTH]</code> <code>Other<wbr>Increase<wbr>Decrease<wbr>In<wbr>Cash<wbr>And<wbr>Cash<wbr>Equivalents</code> &nbsp;·&nbsp; <code>+</code> <code>[CFS]</code> <code>Cash<wbr>And<wbr>Cash<wbr>Equivalents<wbr>Cash<wbr>Flows</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>indirect_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[CFS.NET]</code> <code>Net<wbr>Increase<wbr>Decrease<wbr>In<wbr>Cash<wbr>And<wbr>Cash<wbr>Equivalents</code> &nbsp;·&nbsp; <code>+</code> <code>[CFS]</code> <code>Cash<wbr>And<wbr>Cash<wbr>Equivalents<wbr>Cash<wbr>Flows</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>property</code>, <code>infrastructure</code>, <code>insurance</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>6</code>, <code>A</code>, <code>C</code>, <code>D</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>J</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>61</code>, <code>A1</code>, <code>C1</code>, <code>D1</code>, <code>D2</code>, <code>E3</code>, <code>E5</code>, <code>G4</code>, <code>G5</code>, <code>H1</code>, <code>J1</code>, <code>J2</code>, <code>J3</code>, <code>J4</code>, <code>K1</code>, <code>K2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (5):</b><br/><code>+</code> <code>[CFS.NET]</code> <code>Net<wbr>Increase<wbr>Decrease<wbr>In<wbr>Cash<wbr>And<wbr>Cash<wbr>Equivalents</code> &nbsp;·&nbsp; <code>+</code> <code>[CFS.FX]</code> <code>Effect<wbr>Of<wbr>Exchange<wbr>Rate<wbr>Changes<wbr>On<wbr>Cash<wbr>And<wbr>Cash<wbr>Equivalents</code> &nbsp;·&nbsp; <code>+</code> <code>[CFS.DEC]</code> <code>Cash<wbr>And<wbr>Cash<wbr>Equivalent<wbr>Of<wbr>Deconsolidated<wbr>Subsidiaries</code> &nbsp;·&nbsp; <code>+</code> <code>[CFS.OTH]</code> <code>Other<wbr>Increase<wbr>Decrease<wbr>In<wbr>Cash<wbr>And<wbr>Cash<wbr>Equivalents</code> &nbsp;·&nbsp; <code>+</code> <code>[CFS]</code> <code>Cash<wbr>And<wbr>Cash<wbr>Equivalents<wbr>Cash<wbr>Flows</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>financial_and_sharia</code>, <code>financing</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>C</code>, <code>E</code>, <code>G</code>, <code>H</code>, <code>I</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>C1</code>, <code>E6</code>, <code>G1</code>, <code>G2</code>, <code>G4</code>, <code>G5</code>, <code>H1</code>, <code>I2</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[CFS.NET]</code> <code>Net<wbr>Increase<wbr>Decrease<wbr>In<wbr>Cash<wbr>And<wbr>Cash<wbr>Equivalents</code> &nbsp;·&nbsp; <code>+</code> <code>[CFS.FX]</code> <code>Effect<wbr>Of<wbr>Exchange<wbr>Rate<wbr>Changes<wbr>On<wbr>Cash<wbr>And<wbr>Cash<wbr>Equivalents</code> &nbsp;·&nbsp; <code>+</code> <code>[CFS.OTH]</code> <code>Other<wbr>Increase<wbr>Decrease<wbr>In<wbr>Cash<wbr>And<wbr>Cash<wbr>Equivalents</code> <i>[G1, G2]</i> &nbsp;·&nbsp; <code>+</code> <code>[CFS]</code> <code>Cash<wbr>And<wbr>Cash<wbr>Equivalents<wbr>Cash<wbr>Flows</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>securities</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>G</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>G3</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (4):</b><br/><code>+</code> <code>[CFS.NET]</code> <code>Net<wbr>Increase<wbr>Decrease<wbr>In<wbr>Cash<wbr>And<wbr>Cash<wbr>Equivalents</code> &nbsp;·&nbsp; <code>+</code> <code>[CFS.DEC]</code> <code>Cash<wbr>And<wbr>Cash<wbr>Equivalent<wbr>Of<wbr>Deconsolidated<wbr>Subsidiaries</code> &nbsp;·&nbsp; <code>+</code> <code>[CFS.OTH]</code> <code>Other<wbr>Increase<wbr>Decrease<wbr>In<wbr>Cash<wbr>And<wbr>Cash<wbr>Equivalents</code> &nbsp;·&nbsp; <code>+</code> <code>[CFS]</code> <code>Cash<wbr>And<wbr>Cash<wbr>Equivalents<wbr>Cash<wbr>Flows</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Entry Points:</b><br/><code>collective_investment_contract</code></td>
      <td width="34%" valign="top"><b>Sectors:</b><br/><code>B</code>, <code>K</code></td>
      <td width="32%" valign="top"><b>Subsectors:</b><br/><code>B1</code>, <code>K1</code></td>
    </tr>
    <tr>
      <td width="34%" valign="top"><b>Variant:</b><br/><code>direct_method</code></td>
      <td colspan="2" width="66%" valign="top"><b>Accounts (2):</b><br/><code>+</code> <code>[CFS.NET]</code> <code>Net<wbr>Increase<wbr>Decrease<wbr>In<wbr>Cash<wbr>And<wbr>Cash<wbr>Equivalents</code> &nbsp;·&nbsp; <code>+</code> <code>[CFS]</code> <code>Cash<wbr>And<wbr>Cash<wbr>Equivalents<wbr>Cash<wbr>Flows</code></td>
    </tr>
  </tbody>
</table>

---
