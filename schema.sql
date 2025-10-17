PRAGMA journal_mode=WAL;

CREATE TABLE IF NOT EXISTS wallets (
  address TEXT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS blocks_seen (
  id INTEGER PRIMARY KEY CHECK (id = 0),
  last_block INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS tokens (
  address TEXT PRIMARY KEY,
  symbol TEXT,
  decimals INTEGER
);

CREATE TABLE IF NOT EXISTS erc20_transfers (
  tx_hash TEXT,
  log_index INTEGER,
  blk INTEGER,
  token TEXT,
  from_addr TEXT,
  to_addr TEXT,
  amount TEXT,        -- raw uint256 as text
  PRIMARY KEY (tx_hash, log_index)
);

CREATE TABLE IF NOT EXISTS eth_transfers (
  tx_hash TEXT PRIMARY KEY,
  blk INTEGER,
  from_addr TEXT,
  to_addr TEXT,
  value_wei TEXT
);
