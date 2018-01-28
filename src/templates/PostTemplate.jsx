import React from "react";
import Disqus from "../components/Disqus";
import Meta from "../components/Meta";
import AddThis from "../components/AddThis";
import "katex/dist/katex.min.css";

export default function Template({ data }) {
  const { frontmatter, html, fields: { slug }, excerpt } = data.markdownRemark;

  const description = frontmatter.description || excerpt;

  return (
    <section className="post-container">
      <Meta
        title={frontmatter.title}
        date={frontmatter.date}
        description={description}
        tags={frontmatter.keywords}
      />
      <article className="post">
        <header className="post__header">
          <h2>{frontmatter.title}</h2>
          <p>
            <time>{frontmatter.date}</time>
          </p>
        </header>
        <main
          className="post__body"
          dangerouslySetInnerHTML={{ __html: html }}
        />
      </article>

      <AddThis />
      <Disqus identifier={slug} />
    </section>
  );
}

export const pageQuery = graphql`
  query PostBySlug($slug: String!) {
    markdownRemark(fields: { slug: { eq: $slug } }) {
      html
      excerpt
      frontmatter {
        date(formatString: "MMMM DD, YYYY")
        title
        keywords
        description
      }
      fields {
        slug
      }
    }
  }
`;
