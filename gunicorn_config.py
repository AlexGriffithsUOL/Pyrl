from rq import cpu_count

workers = cpu_count() * 2 + 1