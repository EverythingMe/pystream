# pystream

Stream backups directly to/from S3/HDFS without wasting disk space during the process.  
This tool is a command line interface for the [smart_open](https://pypi.python.org/pypi/smart_open/) library

## Installation

`pip install pystream`

## Usage

Stream `mysqldump` directly to S3 without wasting any additional disk space during the dump process
```
mysqldump | gzip | pystream - s3://backups/mysqldump.gz
```

Restore MySQL backup directly from S3
```
pystream s3://backups/mysqldump.gz - | gunzip | mysql
```

Stream a tarball to S3
```
tar cz . | pystream - s3://backups/backup.tar.gz
```

Stream a tarball from S3
```
pystream s3://backups/backup.tar.gz - | tar xz
```

S3 `cat`
```
pystream s3://bucket/path/to/key -
```

And the usual `s3cmd cp` like usage:
```
pystream s3://bucket/path/to/key /path/on/filesystem

pystream /path/on/filesystem s3://bucket/path/to/key
```
