Some things to note: 

1. .isin() method can be done via df['row'].isin(['x','y','z'])
2. .between() method can be done via:
`df[df['age'].between(25, 35)]  # inclusive on both ends by default`
3. .quey() method: 
`# Standard boolean indexing:``
``df[(df['age'] &gt; 30) &amp; (df['salary'] &gt; 50000) &amp; (df['city'] != 'LA')]``
``
``# Equivalent query:``
``df.query('age &gt; 30 and salary &gt; 50000 and city != "LA"')`
4. to handle NaN, use: 

1. .isNaN()
2. notNaN()



o